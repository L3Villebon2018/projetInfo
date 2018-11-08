from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from .models import PostFilActu

# Chaque suite de tests doit être dans une classe, les fonctions lancées doivent commencer par test_

# Pour executer les tests, py -3 manage.py test


class FilActuTests(TestCase):
    def creer_post(self, supprime=False, titre="Test Post Title", contenu="Test Post Content", couleur="bleu"):
        return PostFilActu.objects.create(supprime=supprime, titre=titre, contenu=contenu, couleur=couleur)

    def test_post_deleted(self):
        """
        Vérifie que la vue détails d'un post "supprimé" ne s'affiche pas
        """
        post = self.creer_post(supprime=True)
        url = reverse('fil-actu-nouveau-commentaire', args=(post.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_post_details(self):
        """
        Vérifie que la vue détails d'un post non "supprimé" s'affiche bien
        """
        post = self.creer_post(supprime=False)
        url = reverse('fil-actu-nouveau-commentaire', args=(post.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_post_not_logged_in(self):
        """
        Vérifie que l'on soit connecté pour pouvoir poster
        """

        self.client.logout()
        url = reverse('fil-actu-nouveau-post')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('login')))




