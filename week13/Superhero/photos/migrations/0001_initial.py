# Generated by Django 4.2.7 on 2023-11-13 18:13

from django.db import migrations, models
import photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=photos.models.get_upload)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
