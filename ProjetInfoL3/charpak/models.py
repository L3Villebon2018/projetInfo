from django.db import models
from django.contrib.auth.models import User
import datetime

from django.utils import timezone


class Ecole(models.Model):
    nom = models.CharField(max_length=150)

    def __str__(self):
        return self.nom


class Formation(models.Model):
    nom = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    type = models.CharField(max_length=150)

    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return str(self.type) + ' | ' + str(self.nom)


class Etudiant(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.DO_NOTHING, default=None, blank=True, null=True)

    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    photo = models.ImageField()

    email = models.CharField(max_length=512)
    telephone = models.CharField(max_length=15)

    promo = models.PositiveSmallIntegerField()
    parain = models.ForeignKey('Etudiant', on_delete=models.CASCADE, default=None, blank=True, null=True)

    profil_bac = models.CharField(max_length=50)

    formation = models.ForeignKey(Formation, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    statut = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom} - Promo {self.promo}"


class PostFilActu(models.Model):
    supprime = models.BooleanField(default=False)

    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)

    titre = models.CharField(max_length=512)
    contenu = models.TextField()

    heure_creation = models.DateTimeField(default=timezone.now)
    heure_modification = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.titre}"


class Commentaire(models.Model):
    post = models.ForeignKey(PostFilActu, on_delete=models.CASCADE, related_name='comments')
    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    text = models.TextField()

    heure_creation = models.DateTimeField(default=timezone.now)
    heure_modification = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"Commentaire sur {self.post.titre}"
