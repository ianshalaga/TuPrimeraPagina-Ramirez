from django import forms
from .models import Game, Album, Song, AlbumSong, GameMode, Stage, Character, Situation


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game_number', 'name']

        # game = forms.ModelChoiceField(
        #     queryset=Game.objects.all(),  # Mostrar todos los juegos existentes
        #     empty_label="Seleccionar juego",
        #     widget=forms.Select(attrs={'class': 'form-control'}),
        #     required=True
        # )


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_number', 'name', 'type']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'other_name', 'duration',
                  'variation_type', 'original_song']


class AlbumSongForm(forms.ModelForm):
    class Meta:
        model = AlbumSong
        fields = ['song_number']


class SituationForm(forms.ModelForm):
    class Meta:
        model = Situation
        # fields = ['description', 'character', 'stage', 'game_mode']
        fields = ['description']


class GameModeForm(forms.ModelForm):
    class Meta:
        model = GameMode
        fields = ['name']


class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['name', 'other_name']


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name']
