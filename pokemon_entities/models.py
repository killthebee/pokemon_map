from django.db import models

class Pokemon(models.Model):
    title = models.TextField()
    picture = models.ImageField(null=True, blank=True, upload_to='pokemon_pics/')
    def __str__(self):
        return self.title