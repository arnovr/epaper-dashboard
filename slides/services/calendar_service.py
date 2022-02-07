from datetime import datetime
from ics import Calendar
import requests
from slides.calendar.calendar_drawing import CalendarDrawing
from slides.slide_runner import SlideRunner
from dateutil import parser

class CalendarService():
    def __init__(self, ics_url):
        self.ics_url = ics_url

    def getNow(self):
        response = requests.get(self.ics_url)
        calendar = Calendar(response.text)

        for event in calendar.timeline.now():
            begin = str(datetime.fromisoformat(str(event.begin)).strftime("%H:%M"))
            end = str(datetime.fromisoformat(str(event.end)).strftime("%H:%M"))

            return {
                "name": event.name,
                "timestamp_start": begin,
                "timestamp_end": end
            }

        return {
            "name": "Nothing today",
            "timestamp_start": "",
            "timestamp_end": ""
        }