from typing import Union

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from collections import defaultdict

from django.utils import timezone
from django.urls import reverse

from .models import PostFilActu, Etudiant, Formation, Promo, Commentaire
from .forms import FilActu_PostForm, FilActu_CommentsForm, index_modifierForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
import logging

# Log
logger = logging.getLogger(__name__)
# Create your views here.

def index(request):
    derniers_posts = PostFilActu.objects.filter(supprime=False).all()[:5]

    return render(request, 'public/index.html', {'derniers_posts': derniers_posts})

@login_required()
def index_arborescence(request):
    formation = request.GET.get('formation', None)
    promo = request.GET.get('promo', None)

    etu_qs = Etudiant.objects

    if formation:
        etu_qs = etu_qs.filter(formation=formation)

    if promo:
        etu_qs = etu_qs.filter(promo=promo)

    etudiants = defaultdict(list)
    for etudiant in etu_qs.all():
        etudiants[etudiant.promo].append(etudiant)

    etudiants = dict(etudiants)
    formations = []
    for formation in Formation.objects.all():
        formations.append(formation)

    return render(request, 'arborescence/index_arborescence.html',
                  {'etudiants_dict': etudiants, 'formations': formations})


@login_required()
def index_profil(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    return render(request, 'profil/index_profil.html', {'etudiant': etudiant})


@login_required()
def index_modifier(request, etudiant_id):
    etudiant = get_object_or_404(Etudiant, pk=etudiant_id)
    parrains = Etudiant.objects.filter(promo=etudiant.promo.promo_parrains).all()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = index_modifierForm(request.POST, request.FILES, instance=etudiant)
        form.fields["parrain"].queryset = parrains
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = form.save()

            # form.save()
            return HttpResponseRedirect(reverse('profil-etudiant', kwargs={'etudiant_id': etudiant_id}))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = index_modifierForm(instance=etudiant)
        form.fields["parrain"].queryset = parrains

    return render(request, 'profil/index_modifier.html', {'etudiant': etudiant, 'form': form})



def index_promo(request, promo_id):
    promo = get_object_or_404(Promo, pk=promo_id)
    return render(request, 'promo/index_promo.html', {'promo': promo})

def index_mentions_legales(request):
    return render(request, 'info_supplementaires/mentions_legales.html')

def index_protection_donnees(request):
    return render(request, 'info_supplementaires/Politiques_protections.html')

def index_FAQ(request):
    return render(request, 'FAQ/index_FAQ.html')


def astuces_FAQ(request):
    return render(request, 'FAQ/astuces_FAQ.html')


def info_FAQ(request):
    return render(request, 'FAQ/info_FAQ.html')


def extra_FAQ(request):
    return render(request, 'FAQ/extra_FAQ.html')

def SiteUtile_FAQ(request):
    return render(request, 'FAQ/SiteUtile_FAQ.html')


def index_Photo(request):
    return render(request, 'Photo/index_Photo.html')


def index_login(request):
    return render(request, 'registration/login.html')


@login_required()
def index_fil_actu(request):
    promos = request.user.etudiant.promo
    posts = PostFilActu.objects.filter(supprime=False, promo_ciblee = promos)
    for post in posts:
        print(post.contenu)
    couleur = []
    for post in posts:
        if post.couleur not in couleur:
            couleur.append(post.couleur)
    b = 'bleu'
    r = 'rouge'
    j = 'jaune'
    ve = 'vert'
    vi = 'violet'
    dict_final = {}
    if b in couleur:
        dict_final[b] = 'Promo'
    if r in couleur:
        dict_final[r] = 'Administration'
    if j in couleur:
        dict_final[j] = 'BDE'
    if ve in couleur:
        dict_final[ve] = 'Public'
    if vi in couleur:
        dict_final[vi] = 'Divers'

    provenance = request.GET.get('trier_par', None)
    if provenance:
        posts = posts.filter(couleur=provenance, supprime=False)
    return render(request, 'fil_actu/index_fil_actu.html', {'posts': posts, 'dict_final': dict_final})


@login_required()
def nouveau_post_fil_actu(request):
    # if this is a POST request we need to process the form data

    possibles_choices = [
                 ('rouge', 'Administration'),
                 ('jaune', 'BDE'),
                 ('violet', 'Divers')]
    if request.user.etudiant:
        user = request.user.etudiant
        if user.membre_bde:
            possibles_choices = [
                ('jaune', 'BDE'),
                ('violet', 'Divers')]
        else:
            possibles_choices = [('violet', 'Divers')]
    else:
        possibles_choices = [
            ('rouge', 'Administration')]


    new_choises = tuple(possibles_choices)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FilActu_PostForm(request.POST, new_choices=new_choises)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            post = form.save(commit=False)

            post.auteur = request.user
            print(post.prive)
            post.save()
            form.save_m2m()
            print(post.promo_ciblee.all())


        # form.save()
            print("PC:" + str(post.promo_ciblee.all()))

            return HttpResponseRedirect('/fil_actu')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilActu_PostForm(new_choices=new_choises)

    #form.fields["promo_ciblee"] .queryset = Promo.objects.order_by('-nom')[:3]
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
def supprime_post(request, post_id):
    post = get_object_or_404(PostFilActu, pk=post_id)

    if post.auteur != request.user:
        return HttpResponseForbidden()

    post.supprime = True
    post.save()
    return HttpResponseRedirect(f'/fil_actu')


@login_required()
def modif_post(request, post_id):
    post = get_object_or_404(PostFilActu, pk=post_id)
    # if this is a POST request we need to process the form data
    if request.user.etudiant:
        user = request.user.etudiant
        if user.membre_bde:
            possibles_choices = [
                ('jaune', 'BDE'),
                ('violet', 'Divers')]
        else:
            possibles_choices = [('violet', 'Divers')]
    else:
        possibles_choices = [
            ('rouge', 'Administration')]
    new_choices = tuple(possibles_choices)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FilActu_PostForm(request.POST, instance=post, new_choices=new_choices)
        # check whether it's valid:
        if form.is_valid():
            post.heure_modification = timezone.now()
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            # form.save()
            return HttpResponseRedirect(f'/fil_actu/{post_id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilActu_PostForm(instance=post, new_choices=new_choices)

    form.fields["promo_ciblee"] .queryset = Promo.objects.order_by('-nom')[:3]
    return render(request, 'fil_actu/nouveau_post_fil_actu.html', {'form': form})


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
            commentaire.heure_modification = timezone.now()
            form.save()
            return HttpResponseRedirect(f'/fil_actu/{post_id}')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilActu_CommentsForm(instance=commentaire)
    return render(request, 'fil_actu/nouveau_commentaire.html', {'form': form, "post": post, "modif": modif})


class BaseRecherche:
    def found(self, query) -> object:
        pass

    def url(self, result) -> str:
        pass


class EtudiantRecherche(BaseRecherche):
    def found(self, query) -> Union[Etudiant, None]:
        res = Etudiant.objects.filter(nom__icontains=query.lower()).first()
        return res

    def url(self, result):
        return reverse('profil-etudiant', kwargs={"etudiant_id": result.id})


class PromoRecherche(BaseRecherche):
    def found(self, query) -> Union[Promo, None]:
        res = Promo.objects.filter(nom=query.lower()).first()

        return res

    def url(self, result):
        return reverse('profil-promo', kwargs={"promo_id": result.id})


class PostRecherche(BaseRecherche):
    def found(self, query) -> Union[PostFilActu, None]:
        res = PostFilActu.objects.filter(titre=query.lower()).first()

        return res

    def url(self, result):
        return reverse("fil-actu-nouveau-commentaire", kwargs={"post_id": result.id})


def rechercher(request):
    terme = request.POST.get("terme")
    #print("terme : ", terme)
    logger.debug("recherche de ", terme, "pour ", request.user)
    if terme:
        moteurs = [EtudiantRecherche(), PromoRecherche(), PostRecherche()]
        result = False
        while not result and len(moteurs) >= 1:
            moteur = moteurs.pop()
            res = moteur.found(terme)
            if res:
                return HttpResponseRedirect(moteur.url(res))
            else:
                logger.warning("not found", terme)


    return HttpResponseRedirect('/')
