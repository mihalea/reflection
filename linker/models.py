from django.db import models

class Project (models.Model):
    sha = models.CharField(max_length=64)
    username = models.CharField(max_length=128)
    repository = models.CharField(max_length=128)
    readme = models.TextField(blank=True)
    image = models.FileField()
