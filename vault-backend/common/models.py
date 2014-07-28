from django.db import models
from django_extensions.db.models import TimeStampedModel
from uuidfield import UUIDField

# Create your models here.

class UUIDModel(TimeStampedModel):
    uuid = UUIDField(auto=True)

    class Meta:
        abstract = True
