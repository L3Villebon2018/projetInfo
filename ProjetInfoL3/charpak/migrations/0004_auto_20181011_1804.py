# Generated by Django 2.1.1 on 2018-10-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charpak', '0003_auto_20181011_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='email',
            field=models.CharField(default='aucun_email@localhost.com', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etudiant',
            name='telephone',
            field=models.CharField(default="0000000000", max_length=15),
            preserve_default=False,
        ),
    ]