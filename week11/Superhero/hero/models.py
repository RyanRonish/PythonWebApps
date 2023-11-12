from django.db import models
from django.urls import reverse_lazy


class Superhero(models.Model):
    name = models.CharField(max_length=200, default="Name")
    identity = models.CharField(max_length=200, default="Identity")
    description = models.TextField(default="Description of Superhero")
    strengths = models.CharField(max_length=200, default="Strengths...")
    weaknesses = models.CharField(max_length=200, default="Weaknesses...")
    image = models.CharField(max_length=200, default="NONE")
    title = models.CharField(max_length=50, default="Article...")
    author = models.CharField(max_length=50, default="Author...")
    article = models.TextField(default="Write your article here...")

    def __str__(self):
        return self.identity
    
    def get_absolute_url(self):
        return reverse_lazy('hero_list')

    
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.identity
    
    def get_absolute_url(self):
        return reverse_lazy('account_edit')
    