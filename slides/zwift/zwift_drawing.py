import os
from slides.drawing import Drawing
from PIL import Image, ImageDraw, ImageFont

class ZwiftDrawing(Drawing):
    def draw(self):
        dirname, filename = os.path.split(os.path.abspath(__file__))
        image = Image.open(os.path.join(dirname, 'dashboard.bmp'))

        draw = ImageDraw.Draw(image)
        #1
        draw.text((5, 0), str(round(self.data["ftp"],1 )) + "w", font=self.font24, fill=0)
        #2
        draw.text((78, 5), str(self.data["totalDistance"]) + " km", font=self.font18, fill=0)
        #3
        draw.text((174, 5), str(self.data["totalDistanceClimbed"]) + " km", font=self.font18, fill=0)
        #4
        draw.text((5, 47), str(self.data["totalTimeInMinutes"]), font=self.font24, fill=0)
        #5
        draw.text((5, 100), str(self.data["lastactivity"]), font=self.font16, fill=0)

        self.epd.display(self.epd.getbuffer(image))