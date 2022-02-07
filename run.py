import os
from dotenv import load_dotenv
from slides.dashboard.dashboard import Dashboard
from slides.email.email import Email

from slides.news.latest_entry_rss_reader import LatestEntryRssReader
from slides.services.calendar_service import CalendarService
from slides.services.imap_service import ImapService
from slides.services.zwift_service import ZwiftService
from slides.slide_factory import SlideFactory
from slides.spotify.spotify import Spotify
from slides.weather.weather import Weather
from slides.calendar.ics_calendar import IcsCalendar
from slides.zwift.zwift_profile import ZwiftProfile
import time

from slides.zwift_activity.zwift_activity_profile import ZwiftActivityProfile

load_dotenv()


zwiftService = ZwiftService(
    os.environ.get("zwift-username"),
    os.environ.get("zwift-password")
)
imapService = ImapService(
    os.environ.get("email-imap"),
    os.environ.get("email-username"),
    os.environ.get("email-password")
);
slideFactory = SlideFactory([
        Dashboard(
            imapService,
            os.environ.get("weather-api-key"),
            zwiftService,
            CalendarService(os.environ.get("ics-url"))
        ),
        Email(
            imapService
        ),
        # Spotify(),
        LatestEntryRssReader(os.environ.get("rssreader-url")),
        Weather(os.environ.get("weather-api-key")),
        IcsCalendar(
            CalendarService(os.environ.get("ics-url"))
        ),
        ZwiftProfile(
            zwiftService
        ),
        ZwiftActivityProfile(
            zwiftService
        )
    ]
)

while True:
    slide = slideFactory.getNext()
    print("Running " + slide.name())
    drawer = slide.run()
    drawer.start()
    drawer.draw()
    drawer.sleep()
    print("Sleeping " + slide.name())
    time.sleep(int(os.environ.get("loopTimeout")))
