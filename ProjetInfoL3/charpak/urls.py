from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('arborescence', views.index_arborescence),
    path('profil/<int:etudiant_id>', views.index_profil),
    path('FAQ', views.index_FAQ),
    path('fil_actu', views.index_fil_actu),
    path('fil_actu/nouveau_post', views.nouveau_post_fil_actu, name="fil-actu-nouveau-post"),
    #path('fil_actu/<int:post_id>', views.nouveau_commentaire, name="fil-actu-details-post"),
    path('fil_actu/<int:post_id>/nouveau_commentaire', views.nouveau_commentaire, name="fil-actu-nouveau-commentaire"),
    path('login', views.index_login),
]