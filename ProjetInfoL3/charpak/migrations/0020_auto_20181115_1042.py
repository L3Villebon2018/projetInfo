# Generated by Django 2.1.3 on 2018-11-15 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charpak', '0019_bde'),
    ]

    operations = [
        migrations.AddField(
            model_name='bde',
            name='porte_parole',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='porte_parle_bde', to='charpak.Etudiant'),
        ),
        migrations.AlterField(
            model_name='bde',
            name='membres',
            field=models.ManyToManyField(default=None, null=True, related_name='membre_bde', to='charpak.Etudiant'),
        ),
    ]
