# Generated by Django 4.2.7 on 2023-11-13 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_remove_photo_author_alter_photo_image_delete_author'),
        ('hero', '0002_alter_superhero_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='superheroes', to='photos.photo'),
        ),
    ]
