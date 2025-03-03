from django.db import models

class DefaultSites(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    featured = models.CharField(max_length=100)
    image = models.ImageField(upload_to='defaultSites/')
