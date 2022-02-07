from datetime import datetime
from ics import Calendar
import requests
from slides.calendar.calendar_drawing import CalendarDrawing
from slides.services.calendar_service import CalendarService
from slides.slide_runner import SlideRunner
from dateutil import parser

class IcsCalendar(SlideRunner):
    def __init__(self, calendarService: CalendarService):
        self.calendarService = calendarService

    def name(self):
        return "Calendar"

    def run(self):
        return CalendarDrawing(self.calendarService.getNow())