import json
import requests

from slides.slide_runner import SlideRunner
from slides.spotify.spotify_drawing import SpotifyDrawing
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Spotify(SlideRunner):
    def __init__(self):
        pass

    def name(self):
        return "spotify"

    def run(self):

        scope = "user-read-currently-playing"

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        currentlyPlaying = sp.currently_playing()
        if currentlyPlaying is None:
            return SpotifyDrawing({
                "artist": "",
                "title": "",
            }); 

        return SpotifyDrawing({
            "artist": currentlyPlaying["item"]["album"]["artists"][0]["name"],
            "title": currentlyPlaying["item"]["name"],
        }); 