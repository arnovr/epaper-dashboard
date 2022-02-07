
import textwrap
from slides.drawing import Drawing
from PIL import Image, ImageDraw, ImageFont


class SpotifyDrawing(Drawing):
    def draw(self):
        image = Image.new('1', (self.epd.height, self.epd.width), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(image)
        
        draw.text((4, 0), self.data["artist"], font=self.font24, fill=0)
        
        y = 30
        lines = textwrap.wrap(str(self.data["title"]), 28);

        for line in lines:
            draw.text((4, y), line, font=self.font18, fill=0)
            y += 20

        self.epd.display(self.epd.getbuffer(image))
