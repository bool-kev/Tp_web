# Generated by Django 5.0.4 on 2024-05-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0005_alter_cour_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cour',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Cours_files'),
        ),
        migrations.AlterField(
            model_name='cour',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='matiere',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Titre'),
        ),
    ]
