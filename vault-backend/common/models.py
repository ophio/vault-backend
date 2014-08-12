from django.db import models
from django_extensions.db.models import TimeStampedModel
from common.fields import AutoUUIDField

# Create your models here.

class UUIDModel(TimeStampedModel):
    id = AutoUUIDField(primary_key=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        try:
            return self.name
        except AttributeError:
            if self.id is not None:
                return self.id
            else:
                return self.__class__.__name__+' object'
