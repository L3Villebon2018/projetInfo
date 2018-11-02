from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class Promo(models.Model):

    CHOIX_COULEURS = (
        ('bleu', 'Bleu'),
        ('rouge', 'Rouge'),
        ('jaune', 'Jaune'),
    )

    nom = models.CharField(max_length=150)
    couleur = models.CharField(max_length=150, choices=CHOIX_COULEURS)

    icone = models.ImageField(default=None, blank=True, null=True, upload_to='images/icones/')

    def __str__(self):
        return f"Promo {self.nom}"


class Ecole(models.Model):
    nom = models.CharField(max_length=150)

    def __str__(self):
        return self.nom


class Formation(models.Model):
    nom = models.CharField(max_length=150)
    domaine = models.CharField(max_length=150)
    type = models.CharField(max_length=150)

    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='formations')

    def __str__(self):
        return str(self.type) + ' | ' + str(self.nom)


class Etudiant(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.DO_NOTHING, default=None, blank=True, null=True)

    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    photo = models.ImageField(default=None, blank=True, null=True, upload_to='images/profils/')

    email = models.CharField(max_length=512, default=None, blank=True, null=True)
    telephone = models.CharField(max_length=15, default=None, blank=True, null=True)

    promo = models.ForeignKey(Promo, on_delete=models.CASCADE, related_name='etudiants')
    parrain = models.ForeignKey('Etudiant', on_delete=models.CASCADE, default=None, blank=True, null=True, related_name='filleuls')

    profil_bac = models.CharField(max_length=50, default=None, blank=True, null=True)

    formation = models.ForeignKey(Formation, on_delete=models.DO_NOTHING, default=None, blank=True, null=True, related_name='etudiants')
    statut = models.CharField(max_length=50, default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} - Promo {self.promo.nom}"


class PostFilActu(models.Model):
    supprime = models.BooleanField(default=False)

    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, blank=True, null=True, related_name='posts')

    titre = models.CharField(max_length=512)
    contenu = models.TextField()

    heure_creation = models.DateTimeField(default=timezone.now)
    heure_modification = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.titre}"


class Commentaire(models.Model):
    supprime = models.BooleanField(default=False)

    post = models.ForeignKey(PostFilActu, on_delete=models.CASCADE, related_name='commentaires')
    auteur = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None, blank=True, null=True, related_name='commentaires')
    contenu = models.TextField()

    heure_creation = models.DateTimeField(default=timezone.now)
    heure_modification = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f"Commentaire sur {self.post.titre}"
