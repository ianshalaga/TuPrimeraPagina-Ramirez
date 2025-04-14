from django.contrib import admin
from .models import Game, Album, Song, AlbumSong, GameMode, Stage, Character, Situation

# Register your models here.


@admin.register(Game)  # admin.site.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["game_number", "name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ["game_number"]


@admin.register(Album)  # admin.site.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["album_number", "game", "name", "type"]
    search_fields = ["name"]
    list_filter = ["game"]
    ordering = ["album_number"]


@admin.register(Song)  # admin.site.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["name", "other_name",
                    "duration", "variation_type", "original_song"]
    search_fields = ["name"]
    list_filter = ["albums", "variation_type"]
    ordering = []


@admin.register(AlbumSong)  # admin.site.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = ["album", "song_number", "song"]
    search_fields = ["song"]
    list_filter = ["album"]
    ordering = ["song_number"]


@admin.register(GameMode)  # admin.site.register(GameMode)
class GameModeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ["name"]


@admin.register(Stage)  # admin.site.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ["name", "other_name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ["name"]


@admin.register(Character)  # admin.site.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ["name"]


@admin.register(Situation)  # admin.site.register(Situation)
class SituationAdmin(admin.ModelAdmin):
    list_display = ["description"]
    search_fields = ["description"]
    list_filter = ["description"]
    ordering = ["description"]
