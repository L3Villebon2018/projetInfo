# Generated by Django 2.1.3 on 2018-11-15 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charpak', '0015_auto_20181114_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='bde',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='membres_bde', to='charpak.Promo'),
        ),
    ]