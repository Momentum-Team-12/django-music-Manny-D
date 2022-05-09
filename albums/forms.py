from django import forms
from .models import Album, Note


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'release_date'
            #'created_at', #don't need this
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'note',
        ]