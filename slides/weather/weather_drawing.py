from slides.drawing import Drawing
from slides.driver.epd import Epd
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps    
import os
import requests

class WeatherDrawing(Drawing):
    def draw(self):
        image = Image.new('1', (self.epd.height, self.epd.width), 255)  # 255: clear the frame
        image.paste(self.icon(), (2,2))
        draw = ImageDraw.Draw(image)
        draw.text((110, 0), str(self.data["description"]), font=self.font24, fill=0)
        draw.text((110, 30), str(self.data["temperature"]) + "C", font=self.font24, fill=0)
        draw.text((110, 60), "Feels like:", font=self.font24, fill=0)
        draw.text((110, 90), str(self.data["temperature_feels_like"]) + "C", font=self.font24, fill=0)
        self.epd.display(self.epd.getbuffer(image))


    def icon(self):
        response = requests.get(
            "http://openweathermap.org/img/wn/" + self.data["icon"] + "@2x.png"
        );

        if response.status_code != 200:
            raise RuntimeError("API Gave incorrect response: " + str(response.status_code))

        file = open("/tmp/weathericon.png", "wb")
        file.write(response.content)
        file.close()

        img = Image.open("/tmp/weathericon.png")
        # img = img.convert("L")
        # img = img.convert("1")
        # img.thumbnail([32, 32])
        return img