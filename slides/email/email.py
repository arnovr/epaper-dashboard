from slides.email.email_drawing import EmailDrawing
from slides.services.imap_service import ImapService

from slides.slide_runner import SlideRunner


class Email(SlideRunner):
    def __init__(self, imapService: ImapService):
        self.imapService = imapService

    def name(self):
        return "email"

    def run(self):
        return EmailDrawing(self.imapService.getLastUnread());