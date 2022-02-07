from datetime import datetime, timedelta
from math import floor
import requests
from slides.dashboard.dashboard_drawing import DashboardDrawing
from zwift import Client
from slides.services.calendar_service import CalendarService
from slides.services.imap_service import ImapService
from slides.services.zwift_service import ZwiftService
from slides.slide_runner import SlideRunner

class Dashboard(SlideRunner):
    def __init__(self, imapService: ImapService, api_key, zwiftService: ZwiftService, calendarService: CalendarService):
        self.api_key = api_key
        self.zwiftService = zwiftService
        self.calendarService = calendarService
        self.imapService = imapService

    def name(self):
        return "Dashboard"

    def run(self):
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather?q=Vleuten&units=metric&appid=" + self.api_key
        );

        if response.status_code != 200:
            raise RuntimeError("API Gave incorrect response: " + str(response.status_code))

        weatherJson = response.json()
        zwift = self.zwiftData();

        return DashboardDrawing({
            "email_unread": self.imapService.getCountUnread(),
            "temperature": weatherJson["main"]["temp"],
            "zwift": zwift,
            "calendar": self.calendarService.getNow()
        }); 

    def zwiftData(self):
        profile = self.zwiftService.profile()

        delta = timedelta(minutes=profile['totalTimeInMinutes'])

        return {
            "ftp": profile['ftp'],
            "totalDistance": floor(profile['totalDistance'] / 1000),
            "totalDistanceClimbed": round(profile['totalDistanceClimbed'] / 1000, 2),
            "totalTimeInMinutes": str(delta),
        }