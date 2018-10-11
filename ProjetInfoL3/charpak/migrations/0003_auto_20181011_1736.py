# Generated by Django 2.1.1 on 2018-10-11 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('charpak', '0002_etudiant_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('heure_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('heure_modification', models.DateTimeField(blank=True, default=None, null=True)),
                ('auteur', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostFilActu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supprime', models.BooleanField()),
                ('titre', models.CharField(max_length=512)),
                ('contenu', models.TextField()),
                ('heure_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('heure_modification', models.DateTimeField(blank=True, default=None, null=True)),
                ('auteur', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='commentaire',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='charpak.PostFilActu'),
        ),
    ]
