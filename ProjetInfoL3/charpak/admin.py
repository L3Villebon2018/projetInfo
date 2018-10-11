from django.contrib import admin

# Register your models here.


from .models import Etudiant, Formation, Ecole
from .models import PostFilActu, Commentaire

admin.site.register(Etudiant)
admin.site.register(Formation)
admin.site.register(Ecole)

admin.site.register(PostFilActu)
admin.site.register(Commentaire)
