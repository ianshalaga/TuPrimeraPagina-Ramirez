from django.shortcuts import render, redirect
from .forms import GameForm, AlbumForm, SongForm, AlbumSongForm, SituationForm
from .models import Song

# Create your views here.


def song(request):
    search = request.GET.get("search", None)
    if search:
        songs = Song.objects.filter(name__icontains=search)
    else:
        songs = Song.objects.all()
    context = {"songs": songs}
    return render(request, 'Music/song.html', context)


def song_create(request):
    if request.method == "POST":
        game_form = GameForm(request.POST, prefix="game")
        album_form = AlbumForm(request.POST, prefix="album")
        song_form = SongForm(request.POST, prefix="song")
        albumsong_form = AlbumSongForm(request.POST, prefix="albumsong")
        situation_form = SituationForm(request.POST, prefix="situation")

        if all([game_form.is_valid(), album_form.is_valid(), song_form.is_valid(), albumsong_form.is_valid()]):
            game = game_form.save()
            album = album_form.save(commit=False)
            album.game = game
            album.save()

            song = song_form.save()

            albumsong = albumsong_form.save(commit=False)
            albumsong.album = album
            albumsong.song = song
            albumsong.save()

            if situation_form.is_valid() and situation_form.cleaned_data.get("description"):
                situation = situation_form.save(commit=False)
                situation.song = song
                situation.save()

            return redirect("music:song")
    else:
        game_form = GameForm(prefix="game")
        album_form = AlbumForm(prefix="album")
        song_form = SongForm(prefix="song")
        albumsong_form = AlbumSongForm(prefix="albumsong")
        situation_form = SituationForm(prefix="situation")

    context = {
        "game_form": game_form,
        "album_form": album_form,
        "song_form": song_form,
        "albumsong_form": albumsong_form,
        "situation_form": situation_form,
    }
    return render(request, "music/song_create.html", context)
