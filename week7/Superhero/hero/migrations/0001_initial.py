# Generated by Django 4.2.7 on 2023-11-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superhero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NONE', max_length=200)),
                ('identity', models.CharField(default='NONE', max_length=200)),
                ('description', models.TextField(default='NONE')),
                ('image', models.CharField(default='NONE', max_length=200)),
                ('strengths', models.CharField(default='NONE', max_length=200)),
                ('weaknesses', models.CharField(default='NONE', max_length=200)),
            ],
        ),
    ]
