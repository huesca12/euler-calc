from django.db import models

# Create your models here.
class Request(models.Model):
    content = models.CharField(max_length=130)
    identifier = models.CharField(max_length=30)
