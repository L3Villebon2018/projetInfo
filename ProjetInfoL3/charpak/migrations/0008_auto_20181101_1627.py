# Generated by Django 2.1.2 on 2018-11-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charpak', '0007_auto_20181101_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='couleur',
            field=models.CharField(choices=[('bleu', 'Bleu'), ('rouge', 'Rouge'), ('jaune', 'Jaune')], max_length=150),
        ),
    ]
