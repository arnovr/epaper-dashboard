from datetime import timedelta
from math import floor
from slides.services.zwift_service import ZwiftService
from slides.zwift.zwift_drawing import ZwiftDrawing
from zwift import Client

from slides.slide_runner import SlideRunner


class ZwiftProfile(SlideRunner):
    def __init__(self, zwiftService: ZwiftService):
        self.zwiftService = zwiftService

    def name(self):
        return "Zwift Profile"

    def run(self):
        profile = self.zwiftService.profile();
        cycler = self.zwiftService.cycler();

        return ZwiftDrawing(
            {
                "name": profile['firstName'],
                "ftp": profile['ftp'],
                "totalDistance": floor(profile['totalDistance'] / 1000),
                "totalDistanceClimbed": round(profile['totalDistanceClimbed'] / 1000, 2),
                "totalTimeInMinutes": str(timedelta(minutes=profile['totalTimeInMinutes'])),
                "lastactivity": cycler.latest_activity["name"],
            }
        );