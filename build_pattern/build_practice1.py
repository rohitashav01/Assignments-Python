class Screen:
    def __init__(self,type):
        self.type=type
    
class Processor:
    def __init__(self,clock_cycle):
        self.clock_cycle=clock_cycle
    
class Fcamera:
    def __init__(self,display):
        self.display = display

class Laptop:
    def __init__(self):
        self.screen = None
        self.processor = None
        self.fcamera = None

    def specification(self):
        print(f"Screen Type:{self.screen.type} \n Processor: {self.processor.clock_cycle},\n Camera Type: {self.fcamera.display}")





