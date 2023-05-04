from django.db import models
from django.urls import reverse

# Create your models here.

class Studio(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Anime(models.Model):
    name = models.CharField(max_length=300)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    releaseYear = models.IntegerField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('anime_detail', kwargs={'anime_id': self.id})
    
