from django.db import models
from common.models import UUIDModel

# Create your models here.

class Platform(UUIDModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

class Developer(UUIDModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    email = models.CharField(max_length=255, null=False, blank=False, unique=True)

class Library(UUIDModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    platform = models.ForeignKey('core.Platform', null=False, blank=False)
    link = models.URLField(null=False, blank=False, unique=True)
    repo_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = (('name', 'platform'))

class LibraryVersion(UUIDModel):
    library = models.ForeignKey('core.Library', null=False, blank=False)
    version = models.CharField(max_length=255, null=False, blank=False)
    link = models.URLField(null=True, blank=True)

    class Meta:
        unique_together = (('library', 'version'))

    def __unicode__(self):
        return str(self.library.name) + str(self.version)

class Project(UUIDModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    platform = models.ForeignKey('core.Platform', null=True, blank=True)

class Post(UUIDModel):
    library = models.ForeignKey('core.LibraryVersion', null=False, blank=False)
    developer = models.ForeignKey('core.Developer', null=False, blank=False)
    project = models.ForeignKey('core.Project', null=False, blank=False)
    verified = models.BooleanField(default=False, null=False, blank=False)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = (('library', 'project', 'developer'))

