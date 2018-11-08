from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from collections import defaultdict
from .models import PostFilActu, Etudiant, Formation, Promo, Commentaire
from .forms import FilActu_PostForm, FilActu_CommentsForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden

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

def index_promo(request, promo_id):
    promo = get_object_or_404(Promo, pk=promo_id)
    return render(request, 'promo/index_promo.html', {'promo': promo})



def index_FAQ(request):
    return render(request, 'FAQ/index_FAQ.html')


def astuces_FAQ(request):
    return render(request, 'FAQ/astuces_FAQ.html')

def info_FAQ(request):
    return render(request, 'FAQ/info_FAQ.html')

def extra_FAQ(request):
    return render(request, 'FAQ/extra_FAQ.html')

def index_login(request):
    return render(request, 'login/../templates/registration/login.html')


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
            return HttpResponseRedirect(f'/fil_actu/{post_id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilActu_CommentsForm()

    return render(request, 'fil_actu/nouveau_commentaire.html', {'form': form, 'post': post})


@login_required()
def supprime_commentaire(request, post_id, commentaire_id):
    commentaire = get_object_or_404(Commentaire, pk=commentaire_id)
    provenance = request.GET.get('provenance', None)

    if commentaire.auteur != request.user:
        return HttpResponseForbidden()

    commentaire.supprime = True
    commentaire.save()
    if provenance == 'index':
        return HttpResponseRedirect(f'/fil_actu#post-{post_id}')
    if provenance == 'detail':
        return HttpResponseRedirect(f'/fil_actu/{post_id}')

@login_required()
def modif_commentaire(request, post_id, commentaire_id):
    commentaire = get_object_or_404(Commentaire, pk=commentaire_id)
    post = get_object_or_404(PostFilActu, pk=post_id)
    modif = True
    if commentaire.auteur != request.user:
        return HttpResponseForbidden()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FilActu_CommentsForm(request.POST, instance=commentaire)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/fil_actu/{post_id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilActu_CommentsForm(instance=commentaire)
    return render(request, 'fil_actu/nouveau_commentaire.html', {'form': form, "post": post, "modif": modif})



