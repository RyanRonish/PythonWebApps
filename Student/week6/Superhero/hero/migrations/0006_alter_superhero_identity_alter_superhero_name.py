# Generated by Django 4.2.7 on 2023-11-07 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0005_alter_superhero_description_alter_superhero_identity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='identity',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='superhero',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
