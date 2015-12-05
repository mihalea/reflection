from django.db import models

class Project (models.Model):
    origin = models.URLField()
    alias = models.CharField(max_length=64)
    latest_sha = model.CharField(max_length=64)
    title = model.CharField(max_length=64)
    content = model.TextField()
