from django.forms import ModelForm
from .models import PostFilActu


class FilActu_PostForm(ModelForm):
    class Meta:
        model = PostFilActu
        fields = ['titre', 'contenu']