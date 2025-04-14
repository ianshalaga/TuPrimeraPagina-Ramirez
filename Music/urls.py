from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path("song/", views.song, name="song"),
    path("song-create/", views.song_create, name="song_create"),
]
