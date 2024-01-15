from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:song_id>/", views.song_details, name="song_details"),
    path("add_song/", views.add_song, name="add_song"),
    path("add_artist/", views.add_artist, name="add_artist"),
    path("artist_details/", views.artist_details, name="artist_details"),
]
