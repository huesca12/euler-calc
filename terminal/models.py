from django.db import models

# Create your models here.
class Request(models.Models):
    content = model.CharField(max_length=130)
