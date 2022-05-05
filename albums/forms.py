from django import forms
from .models import Album, Note


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            # 'created_at',
            # 'city',
            # 'state',
            # 'zip_code',
            # 'phone_number',
            # 'email',
            # 'birthday',
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'note',
        ]