from django.db import models


class Ecole(models.Model):
    nom = models.CharField(max_length=150)


class Formation(models.Model):
    nom = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    type = models.CharField(max_length=150)

    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE, default=None, blank=True, null=True)


class Etudiant(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    photo = models.ImageField()

    promo = models.PositiveSmallIntegerField()
    parain = models.ForeignKey('Etudiant', on_delete=models.CASCADE, default=None, blank=True, null=True)

    profil_bac = models.CharField(max_length=50)

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, default=None, blank=True, null=True)
    statut = models.CharField(max_length=50)
