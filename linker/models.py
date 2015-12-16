from django.db import models

class Project (models.Model):
    sha = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    content = models.TextField()
    watched = models.BooleanField()
