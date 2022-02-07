from datetime import timedelta
from math import floor
from zwift import Client
from slides.services.zwift_service import ZwiftService

from slides.slide_runner import SlideRunner
from slides.zwift_activity.zwift_activity_drawing import ZwiftActivityDrawing


class ZwiftActivityProfile(SlideRunner):
    def __init__(self, zwiftService: ZwiftService):
        self.zwiftService = zwiftService

    def name(self):
        return "Zwift Activity"

    def run(self):
        cycler = self.zwiftService.cycler()

        delta = timedelta(seconds=floor(cycler.latest_activity['movingTimeInMs'] / 1000))
        return ZwiftActivityDrawing(
            {
                "name": cycler.latest_activity["name"],
                "averageWatt": round(cycler.latest_activity['avgWatts']),
                "distanceInMeters": floor(cycler.latest_activity['distanceInMeters'] / 1000),
                "totalElevation": floor(cycler.latest_activity['totalElevation']),
                "duration": str(delta),
            }
        );