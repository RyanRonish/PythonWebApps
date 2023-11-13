from django.db import models
from django.urls import reverse_lazy

from photos.models import Photo


class Superhero(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200)
    image = models.CharField(max_length=10, default=" ")
    #image = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True, blank=True, related_name='superheroes')
    description = models.TextField(default="None")
    strengths = models.CharField(max_length=200, default="None")
    weaknesses = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.identity

    def get_absolute_url(self):
        return reverse_lazy('hero_list')