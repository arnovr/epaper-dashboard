from datetime import datetime
from slides.drawing import Drawing
from slides.driver.epd import Epd
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps    
import os
import requests

class DashboardDrawing(Drawing):
    def draw(self):
        dirname, filename = os.path.split(os.path.abspath(__file__))
        image = Image.open(os.path.join(dirname, 'dashboard.bmp'))
        bmp = Image.open(os.path.join(dirname, 'mail.bmp'))
        #mail icon
        image.paste(bmp, (90,5))

        draw = ImageDraw.Draw(image)
        #temp
        draw.text((5, 0), str(round(self.data["temperature"],1 )) + "C", font=self.font24, fill=0)

        #time
        time = datetime.now()
        # draw.text((90, 0), str(time.strftime("%H:%M")), font=self.font24, fill=0)
        draw.text((130, 0), str(self.data["email_unread"]), font=self.font24, fill=0)

        #FTP
        draw.text((185, 0), str(self.data["zwift"]["ftp"]) + "w", font=self.font24, fill=0)

        #date
        draw.text((5, 42), str(time.strftime("%d %b %Y")), font=self.font32, fill=0)

        #calendar
        draw.text((5, 90), str(self.data["calendar"]["timestamp_start"]) + " - " + str(self.data["calendar"]["timestamp_end"]), font=self.font16, fill=0)
        draw.text((5, 105), str(self.data["calendar"]["name"]), font=self.font16, fill=0)

        self.epd.display(self.epd.getbuffer(image))