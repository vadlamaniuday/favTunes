from django.contrib import admin
from .models import Artist, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "artist")
    list_filter = ("artist",)
    search_fields = ("title", "artist__name")


# Register your models here.
admin.site.register(Artist)
admin.site.register(Song, SongAdmin)
