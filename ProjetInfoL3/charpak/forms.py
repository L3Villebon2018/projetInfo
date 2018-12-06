from django.forms import ModelForm,forms
from .models import PostFilActu, Commentaire,Etudiant


class FilActu_PostForm(ModelForm):
    class Meta:
        model = PostFilActu
        fields = ['titre','prive','promo_ciblee' ,'couleur', 'contenu']
        labels = {
            'couleur':"Catégorie du post",
            'promo_ciblee':"Pour qui ?",
            'prive':"Statut"
        }

class FilActu_CommentsForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        labels = {
            'contenu':"Votre commentaire",
        }

class index_modifierForm(ModelForm):
    class Meta:
        model = Etudiant
        fields = ["photo",'email','telephone',"parrain","profil_bac","formation","statut",]

