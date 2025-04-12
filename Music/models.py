from django.db import models
from django.utils.translation import gettext_lazy as _


# ENUMS

class GameNameEnum(models.TextChoices):
    SE = "SE", _("Soul Edge")
    SB = "SB", _("Soul Blade")
    SC = "SC", _("Soulcalibur")
    SCII = "SCII", _("Soulcalibur II")
    SCIII = "SCIII", _("Soulcalibur III")
    SCL = "SCL", _("Soulcalibur Legends")
    SCIV = "SCIV", _("Soulcalibur IV")
    SCBD = "SCBD", _("Soulcalibur: Broken Destiny")
    SCV = "SCV", _("Soulcalibur V")
    SCVI = "SCVI", _("Soulcalibur VI")


class VariationTypeEnum(models.TextChoices):
    ORI = "ORI", _("Original")
    ARR = "ARR", _("Arranged")
    EXT = "EXT", _("Extended")
    SHORT = "SHORT", _("Shortened")
    FRAG = "FRAG", _("Fragment")


class AlbumTypeEnum(models.TextChoices):
    OST = "OST", _("Original Soundtrack")
    GR = "GR", _("Gamerip")


# MODELS

class Game(models.Model):
    game_number = models.PositiveIntegerField()
    name = models.CharField(max_length=10, choices=GameNameEnum.choices)

    def __str__(self):
        return self.get_name_display()


class Album(models.Model):
    album_number = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=5, choices=AlbumTypeEnum.choices)
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name="albums")

    def __str__(self):
        return f"{self.name} ({self.get_type_display()}) | {self.game.get_name_display()}"


class Song(models.Model):
    song_number = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=10)
    albums = models.ManyToManyField(Album, related_name="songs")
    variation_type = models.CharField(
        max_length=6,
        choices=VariationTypeEnum.choices,
        default=VariationTypeEnum.ORI
    )
    original_song = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="variations"
    )

    def __str__(self):
        return self.name


class GameMode(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255)
    stages = models.ManyToManyField(Stage, related_name="characters")

    def __str__(self):
        return self.name


class Situation(models.Model):
    description = models.TextField()
    song = models.ForeignKey(
        Song, on_delete=models.CASCADE, related_name="situations")
    character = models.ForeignKey(
        Character, null=True, blank=True, on_delete=models.SET_NULL)
    stage = models.ForeignKey(
        Stage, null=True, blank=True, on_delete=models.SET_NULL)
    game_mode = models.ForeignKey(
        GameMode, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.description
