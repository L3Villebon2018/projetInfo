from django.forms import ModelForm
from .models import PostFilActu, Commentaire


class FilActu_PostForm(ModelForm):
    class Meta:
        model = PostFilActu
        fields = ['titre', 'couleur', 'contenu']
        labels = {
            'couleur':"Catégorie du post",
        }

class FilActu_CommentsForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        labels = {
            'contenu':"Votre commentaire",
        }