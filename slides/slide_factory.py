from slides.slide_runner import SlideRunner


class SlideFactory:
    def __init__(self, slides):
        self.slides = slides
        self.numberOfSlides = len(slides)
        self.num = 0

    def get(self, name):
        return self.slides[name]

    def getNext(self) -> SlideRunner:
        slide = self.slides[self.num]

        self.num += 1
        if self.num == len(self.slides):
            self.num = 0

        return slide

