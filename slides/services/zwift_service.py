from datetime import timedelta
from math import floor
from slides.zwift.zwift_drawing import ZwiftDrawing
from zwift import Client

from slides.slide_runner import SlideRunner


class ZwiftService():
    def __init__(self, username, password):
        self.client = Client(username, password)

    def cycler(self):
        return self.client.get_profile('me');

    def profile(self):
        cycler = self.client.get_profile('me');
        profile = cycler.profile
        if profile is None:
            raise RuntimeError("Could not load profile")

        return profile