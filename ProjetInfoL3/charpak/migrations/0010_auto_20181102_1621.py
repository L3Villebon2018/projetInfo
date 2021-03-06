# Generated by Django 2.1.2 on 2018-11-02 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charpak', '0009_commentaire_supprime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='auteur',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='commentaires', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='formation',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='etudiants', to='charpak.Formation'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='parain',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filleuls', to='charpak.Etudiant'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='promo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etudiants', to='charpak.Promo'),
        ),
        migrations.AlterField(
            model_name='formation',
            name='ecole',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formations', to='charpak.Ecole'),
        ),
        migrations.AlterField(
            model_name='postfilactu',
            name='auteur',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
