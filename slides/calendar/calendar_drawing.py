import os
import textwrap
from slides.drawing import Drawing
from PIL import Image, ImageDraw, ImageFont

class CalendarDrawing(Drawing):
    def draw(self):
        dirname, filename = os.path.split(os.path.abspath(__file__))
        image = Image.new('1', (self.epd.height, self.epd.width), 255)  # 255: clear the frame
        bmp = Image.open(dirname + '/calendar-icon.bmp')
        image.paste(bmp, (2,2))
        draw = ImageDraw.Draw(image)
        draw.text((40, 5), str(self.data["timestamp_start"]) + " - " + str(self.data["timestamp_end"]), font=self.font24, fill=0)

        y = 40
        lines = textwrap.wrap(str(self.data["name"]), 28);

        for line in lines:
            draw.text((2, y), line, font=self.font18, fill=0)
            y += 20
            
        self.epd.display(self.epd.getbuffer(image))