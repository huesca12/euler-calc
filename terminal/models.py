from django.db import models

import uuid

# Create your models here.
class RawRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=130)
