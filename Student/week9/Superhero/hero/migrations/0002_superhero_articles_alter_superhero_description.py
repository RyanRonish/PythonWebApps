# Generated by Django 4.2.7 on 2023-11-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='articles',
            field=models.TextField(default='Write your article here...'),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='description',
            field=models.TextField(default='Description of Superhero'),
        ),
    ]
