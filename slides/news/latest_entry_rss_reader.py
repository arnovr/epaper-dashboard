import feedparser
import requests

from slides.slide_runner import SlideRunner
from slides.news.rss_drawing import RssDrawing


class LatestEntryRssReader(SlideRunner):
    def __init__(self, url):
        self.url = url

    def name(self):
        return "RssReader"

    def run(self):
        response = requests.get(self.url);
        feed = feedparser.parse(response.text)
        if feed.entries is None:
            raise RuntimeError("No results")

        return RssDrawing({"title": feed.entries[0].title})
