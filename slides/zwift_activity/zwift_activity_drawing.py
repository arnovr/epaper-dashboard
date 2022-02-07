import os
from slides.drawing import Drawing
from PIL import Image, ImageDraw, ImageFont

class ZwiftActivityDrawing(Drawing):
    def draw(self):
        dirname, filename = os.path.split(os.path.abspath(__file__))
        image = Image.open(os.path.join(dirname + '/../', 'dashboard.bmp'))

        draw = ImageDraw.Draw(image)
        #1
        draw.text((5, 0), str(round(self.data["averageWatt"],1 )) + "w", font=self.font24, fill=0)
        #2
        draw.text((78, 0), str(self.data["distanceInMeters"]) + " km", font=self.font24, fill=0)
        #3
        draw.text((174, 0), str(self.data["totalElevation"]) + " m", font=self.font24, fill=0)
        #4
        draw.text((5, 47), str(self.data["duration"]), font=self.font24, fill=0)
        #5
        draw.text((5, 100), str(self.data["name"]), font=self.font16, fill=0)

        self.epd.display(self.epd.getbuffer(image))