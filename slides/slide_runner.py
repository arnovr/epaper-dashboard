from abc import abstractmethod

from slides.drawing import Drawing


class SlideRunner:
    @abstractmethod
    def name(self): raise NotImplementedError

    @abstractmethod
    def run(self) -> Drawing: raise NotImplementedError
