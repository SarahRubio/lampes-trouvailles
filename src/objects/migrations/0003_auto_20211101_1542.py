# Generated by Django 3.1.2 on 2021-11-01 14:42

from django.db import migrations, models
import objects.models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0002_auto_20211101_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='finding',
            name='fourth_image',
            field=models.FileField(blank=True, help_text="Assurez vous que l'image n'est pas trop lourde.", null=True, upload_to=objects.models.logo_upload_to_4, verbose_name='photo n°4'),
        ),
        migrations.AddField(
            model_name='furniture',
            name='fourth_image',
            field=models.FileField(blank=True, help_text="Assurez vous que l'image n'est pas trop lourde.", null=True, upload_to=objects.models.logo_upload_to_4, verbose_name='photo n°4'),
        ),
        migrations.AddField(
            model_name='light',
            name='fourth_image',
            field=models.FileField(blank=True, help_text="Assurez vous que l'image n'est pas trop lourde.", null=True, upload_to=objects.models.logo_upload_to_4, verbose_name='photo n°4'),
        ),
    ]
