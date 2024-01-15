from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Song
from .forms import SongForm, ArtistForm
from GroovyRhythm import models
from django.db.models import Count

# Create your views here.


def index(request):
    songs = Song.objects.all()
    return render(request, "GroovyRhythm/index.html", {"songs": songs})


def song_details(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    return render(request, "GroovyRhythm/song_details.html", {"song": song})


def add_song(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = SongForm()

    return render(request, "GroovyRhythm/add_songs.html", {"form": form})


def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  # Redirect to the home page or any other page
    else:
        form = ArtistForm()

    return render(request, "GroovyRhythm/add_artist.html", {"form": form})


def artist_details(request):
    artists_with_song_count = Artist.objects.annotate(song_count=Count("songs"))
    return render(
        request,
        "GroovyRhythm/artist_details.html",
        {"artists_with_song_count": artists_with_song_count},
    )
