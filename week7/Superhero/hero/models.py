from django.db import models
from django.urls import reverse_lazy


class Superhero(models.Model):
    name = models.CharField(max_length=200, default="NONE")
    identity = models.CharField(max_length=200, default="NONE")
    description = models.TextField(default="NONE")
    image = models.CharField(max_length=200, default="NONE")
    strengths = models.CharField(max_length=200, default="NONE")
    weaknesses = models.CharField(max_length=200, default="NONE")

    def __str__(self):
        return self.identity
    
    def get_absolute_url(self):
        return reverse_lazy('hero_list')
    