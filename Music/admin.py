from django.contrib import admin
from .models import Game, Album, Song, GameMode, Stage, Character, Situation

# Register your models here.

admin.site.register(Game)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(GameMode)
admin.site.register(Stage)
admin.site.register(Character)
admin.site.register(Situation)
