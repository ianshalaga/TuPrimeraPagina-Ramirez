# Generated by Django 5.2 on 2025-04-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0003_remove_song_albums_remove_song_song_number_albumsong_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='stages',
            field=models.ManyToManyField(blank=True, null=True, related_name='characters', to='Music.stage'),
        ),
        migrations.AlterField(
            model_name='situation',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
