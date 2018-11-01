from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from collections import defaultdict
from .models import PostFilActu, Etudiant, Formation, Promo
from .forms import FilActu_PostForm, FilActu_CommentsForm
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'public/index.html')


def index_arborescence(request):
    promo = list(Promo.objects.all())
    etudiants = defaultdict(list)
    for etudiant in Etudiant.objects.all():
        etudiants[etudiant.promo].append(etudiant)

    etudiants = dict(etudiants)
    formations = []
    for formation in Formation.objects.all():
        formations.append(formation)

    return render(request, 'arborescence/index_arborescence.html', {'etudiants_dict': etudiants, 'formations': formations})

def index_profil(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    return render(request, 'profil/index_profil.html', {'etudiant': etudiant})


def index_FAQ(request):
    return render(request, 'FAQ/index_FAQ.html')

def index_login(request):
    return render(request, 'login/login.html')


def index_fil_actu(request):
    posts = PostFilActu.objects.all()
    return render(request, 'fil_actu/index_fil_actu.html', {'posts': posts})


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

            # form.save()
            return HttpResponseRedirect('/fil_actu')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilActu_PostForm()

    return render(request, 'fil_actu/nouveau_post_fil_actu.html', {'form': form})


@login_required()
def nouveau_commentaire(request, post_id):
    post = get_object_or_404(PostFilActu, pk=post_id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FilActu_CommentsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            commentaire = form.save(commit=False)
            commentaire.post = post
            commentaire.auteur = request.user
            commentaire.save()

            # form.save()
            return HttpResponseRedirect('/fil_actu')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilActu_CommentsForm()

    return render(request, 'fil_actu/nouveau_commentaire.html', {'form': form})
