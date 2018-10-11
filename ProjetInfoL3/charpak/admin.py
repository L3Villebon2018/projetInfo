from django.contrib import admin

# Register your models here.


from .models import Etudiant, Formation, Ecole

admin.site.register(Etudiant)
admin.site.register(Formation)
admin.site.register(Ecole)
