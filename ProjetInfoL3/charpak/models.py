from django.db import models


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
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    photo = models.ImageField()

    promo = models.PositiveSmallIntegerField()
    parain = models.ForeignKey('Etudiant', on_delete=models.CASCADE, default=None, blank=True, null=True)

    profil_bac = models.CharField(max_length=50)

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, default=None, blank=True, null=True)
    statut = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.prenom} {self.nom} - Promo {self.promo}"
