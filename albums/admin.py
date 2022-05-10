from django.contrib import admin
from .models import Album
from .models import Note

admin.site.register(Album)
admin.site.register(Note)