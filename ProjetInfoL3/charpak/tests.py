from test_plus.test import TestCase as PlusTestCase


class TestCase(PlusTestCase):
    pass


# Create your tests here.
from django.urls import reverse

from .models import PostFilActu, Commentaire


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

    def test_post_index(self):
        """
        Vérifie que la vue d'index ne s'affiche que quand un utilisateur est connecté
        """
        self.assertLoginRequired('fil-actu-index')

        user1 = self.make_user('u1')


        post = self.creer_post(supprime=False)
        with self.login(username=user1.username, password='password'):
            self.get_check_200('fil-actu-index')

    def test_post_details(self):
        """
        Vérifie que la vue détails d'un post non "supprimé" s'affiche bien
        """
        post = self.creer_post(supprime=False)
        user1 = self.make_user('u1')

        self.assertLoginRequired('fil-actu-nouveau-commentaire', post.id)

        with self.login(username=user1.username, password='password'):
            self.get_check_200('fil-actu-nouveau-commentaire', post.id)

    def test_new_post_restrictions(self):
        """
        Vérifie que l'on soit connecté pour pouvoir poster
        """

        VUE = "fil-actu-nouveau-post"
        self.assertLoginRequired(VUE)

        user1 = self.make_user('u1')

        with self.login(username=user1.username, password='password'):
            response = self.get_check_200(VUE)


class ModelTests(TestCase):
    def creer_post(self, supprime=False, titre="Test Post Title", contenu="Test Post Content", couleur="bleu"):
        return PostFilActu.objects.create(supprime=supprime, titre=titre, contenu=contenu, couleur=couleur)

    def ajouter_commentaire(self, post, supprime=False, contenu="Contenu d'un commentaire de test"):
        return Commentaire.objects.create(post=post, supprime=supprime, contenu=contenu)

    def test_taille_commenatires_visibles_minimal(self):
        post = self.creer_post()
        c1 = self.ajouter_commentaire(post)
        c2 = self.ajouter_commentaire(post, supprime=True)

        self.assertTrue(post.commentaires_visibles.count() == 1)
        self.assertIn(c1, post.commentaires_visibles.all())

    def test_taille_commenatires_visibles_10_comments(self):
        post = self.creer_post()

        c1 = self.ajouter_commentaire(post)
        c2 = self.ajouter_commentaire(post, supprime=True)
        c3 = self.ajouter_commentaire(post)
        c4 = self.ajouter_commentaire(post)
        c5 = self.ajouter_commentaire(post, supprime=True)
        c6 = self.ajouter_commentaire(post, supprime=True)
        c7 = self.ajouter_commentaire(post, supprime=True)
        c8 = self.ajouter_commentaire(post, supprime=True)
        c9 = self.ajouter_commentaire(post)
        c10 = self.ajouter_commentaire(post)

        self.assertTrue(post.commentaires_visibles.count() == 5)
        self.assertIn(c1, post.commentaires_visibles)
