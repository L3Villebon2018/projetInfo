# Generated by Django 2.1.3 on 2018-11-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charpak', '0018_auto_20181115_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default="BDE de l'institut", max_length=150)),
                ('annee', models.IntegerField()),
                ('membres', models.ManyToManyField(to='charpak.Etudiant')),
            ],
        ),
    ]
