from django.forms import ModelForm
from .models import PostFilActu, Commentaire


class FilActu_PostForm(ModelForm):
    class Meta:
        model = PostFilActu
        fields = ['titre', 'contenu', 'couleur']

class FilActu_CommentsForm(ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        labels = {
            'contenu':"Votre commentaire",
        }