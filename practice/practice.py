"""
class Person:
 
    name="Jatin"
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person()
Person.say_hi(p)
"""

def show():
    print("this function shows the data")

def sum(a,b):
    return f"Sum is:{a+b}"

print(__name__)


if __name__=='__main__':
    show()
    res=sum(10,20)
    print(res)

   