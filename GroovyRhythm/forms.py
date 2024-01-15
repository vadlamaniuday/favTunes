from django import forms
from .models import Song, Artist


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "artist"]

    artist = forms.ModelChoiceField(queryset=Artist.objects.all())


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ["name"]
