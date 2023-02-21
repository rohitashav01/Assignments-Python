from build_practice1 import *

class LaptopBuilder:
    def add_screen(self):
        pass

    def add_processor(self):
        pass

    def add_fcamera(self):
        pass
    
    def build(self):
        pass


class AsusBuild(LaptopBuilder):
    def __init__(self):
        self.laptop = Laptop()

    def add_screen(self):
        screen = Screen("Matt Finish")
        self.laptop.screen = screen
        return self

    def add_processor(self):
        processor=Processor("2.4 GHz")
        self.laptop.processor = processor
        return self
    
    def add_fcamera(self):
        fcamera = Fcamera("Digital")
        self.laptop.fcamera = fcamera
        return self
    
    def build(self):
        return self.laptop