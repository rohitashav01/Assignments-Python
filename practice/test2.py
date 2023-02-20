
class Singleton:
   
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
a = Singleton()
a.data = "object"
print(a.data)
b = Singleton()
print(b.data)

"""
class emp:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
  
    def show(self):
        print(self.name)
        print(self.salary)
  
e1 = emp("arun",9000)

print("Dictionary form :", vars(e1))
print(dir(e1))
"""
