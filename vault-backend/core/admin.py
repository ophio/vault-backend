from django.contrib import admin
from core.models import Platform, Developer, Library, LibraryVersion, Project, Post

# Register your models here.

admin.site.register(Platform)
admin.site.register(Developer)
admin.site.register(Library)
admin.site.register(LibraryVersion)
admin.site.register(Project)
admin.site.register(Post)
