from django.forms import ModelForm,forms
from .models import PostFilActu, Commentaire,Etudiant


class FilActu_PostForm(ModelForm):
    class Meta:
        model = PostFilActu
        fields = ['titre','prive','promo_ciblee' ,'couleur', 'contenu']
        labels = {
            'couleur':"Catégorie du post",
            'promo_ciblee':"Pour qui ?",
            'prive':"Privé ? (Seulement les promos ciblees ci dessous pourront accéder au post) "
        }

    def __init__(self, *args, **kwargs):
        new_choices = kwargs.pop("new_choices")
        super().__init__(*args, **kwargs)
        self.fields['couleur'].choices = new_choices

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

