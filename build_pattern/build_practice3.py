from build_practice2 import *

class Director:
    def __init__(self,laptop_builder):
        self.laptop_builder = laptop_builder

    def get_laptop(self):
        return self.laptop_builder.add_screen().add_processor().add_fcamera().build()



def main():
    asus_build = AsusBuild()
    director = Director(asus_build)
    
    laptop = director.get_laptop()
    laptop.specification()


if __name__=="__main__":
    main()