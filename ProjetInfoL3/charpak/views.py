from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import PostFilActu
from .forms import FilActu_PostForm
# Create your views here.

def index(request):
    return render(request, 'public/index.html')

def index_arborescence(request):
    return render(request, 'arborescence/index_arborescence.html')

def index_FAQ(request):
    return render(request, 'FAQ/index_FAQ.html')

def index_fil_actu(request):
    posts = PostFilActu.objects.all()
    return render(request, 'fil_actu/index_fil_actu.html', {'posts' : posts})

@login_required()
def nouveau_post_fil_actu(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FilActu_PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            post = form.save(commit=False)
            post.auteur = request.user
            post.save()

            #form.save()
            return HttpResponseRedirect('/fil_actu')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilActu_PostForm()

    return render(request, 'fil_actu/nouveau_post_fil_actu.html', {'form': form})