from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    release_date = models.DateField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="notes")
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.TextField(max_length=500)