from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('arborescence', views.index_arborescence, name="arborescence-index"),
    path('profil/<int:etudiant_id>', views.index_profil, name="profil-etudiant"),
    path('modifier/<int:etudiant_id>', views.index_modifier, name="modifier-etudiant"),
    path('promo/<int:promo_id>', views.index_promo, name="profil-promo"),
    path('FAQ', views.index_FAQ, name="FAQ-index"),
    path('FAQ/astuces', views.astuces_FAQ, name="FAQ-astuces"),
    path('FAQ/extra', views.extra_FAQ, name="FAQ-extra"),
    path('FAQ/info', views.info_FAQ, name="FAQ-info"),
    path('FAQ/SiteUtile', views.SiteUtile_FAQ, name="FAQ-site"),
    path('fil_actu', views.index_fil_actu, name="fil-actu-index"),
    path('fil_actu/nouveau_post', views.nouveau_post_fil_actu, name="fil-actu-nouveau-post"),
    path('fil_actu/<int:post_id>', views.nouveau_commentaire, name="fil-actu-nouveau-commentaire"),
    path('fil_actu/<int:post_id>/<int:commentaire_id>/supprime_commentaire', views.supprime_commentaire, name="fil-actu-supprime-commentaire"),
    path('fil_actu/<int:post_id>/supprime_post', views.supprime_post, name="fil-actu-supprime-post"),
    path('fil_actu/<int:post_id>/<int:commentaire_id>/modif_commentaire', views.modif_commentaire, name="fil-actu-modif-commentaire"),
    path('fil_actu/<int:post_id>/modif_commentaire', views.modif_post, name="fil-actu-modif-post"),
    path('registration/login/', views.index_login, name="login"),
    path('photo/index', views.index_Photo, name="Photo-index"),
    path('recherche', views.rechercher, name="recherche"),
    path('info_supplementaires/mentions_legales', views.index_mentions_legales, name="Mentions_Legales"),
    path('info_supplementaires/protection_donnees', views.index_protection_donnees, name="Protection_donnees")
]