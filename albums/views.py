from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .models import Note
from .forms import AlbumForm
from .forms import NoteForm


# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html", {"albums": albums})


def new_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/new_album.html", {"form": form})


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_album.html", {
        "form": form,
        "album": album
    })


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_album.html", {"album": album})


def notes_album(request, pk): 
    album = get_object_or_404(Album, pk=pk)

    return render(request, "albums/notes_album.html", {"album": album})

def add_note(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.album = album
            new_note.save()
            return redirect(to='notes_album' ,pk=pk)

    return render(request, "albums/add_note.html", {
        "form": form,
        "album": album
    })