from django.db import models

class Project (models.Model):
    origin = models.URLField()
    latest_sha = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    content = models.TextField()
