import os
from slides.driver.epd import Epd
from PIL import Image, ImageDraw, ImageFont

class Drawing:
    def __init__(self, data: dict):
        self.data = data
        self.epd = Epd()
        driverdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'slides/driver')
        self.font32 = ImageFont.truetype(os.path.join(driverdir, 'Font.ttc'), 32)
        self.font24 = ImageFont.truetype(os.path.join(driverdir, 'Font.ttc'), 24)
        self.font18 = ImageFont.truetype(os.path.join(driverdir, 'Font.ttc'), 18)
        self.font16 = ImageFont.truetype(os.path.join(driverdir, 'Font.ttc'), 16)

    def start(self): 
        self.epd.init(self.epd.FULL_UPDATE)
        # self.epd.Clear(0xFF)

    def draw(self): raise NotImplementedError()

    def sleep(self):
        self.epd.sleep()