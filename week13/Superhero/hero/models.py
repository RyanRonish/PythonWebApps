from django.db import models
from django.urls import reverse_lazy

from photos.models import Photo


class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', db_column='image_id', default="Image not available")  # Set db_column to 'image_id'
    #image = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(default="None")
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')