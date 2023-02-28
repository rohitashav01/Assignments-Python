""""
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

"""
class Human:
    data= "object"
    def __init___(self, *args, **kwargs):
        if not hasattr(self, '_instance'):
            self._instance = super().__init__(self, *args, **kwargs)
        else:
            print("Class can have only object")
    
a = Human()
print(a.data)
b=Human()
print(b.data) 
"""
"""
class Singleton:
    _instance=None
    
    def __new__(cls):
        try:
            if cls._instance is None:
                print("Creating object")
                cls._instance = super(Singleton,cls).__new__(cls)
        except:
            print("Your class can have only one object")

obj1=Singleton()
print(obj1)

obj2=Singleton()
print(obj2)
"""
"""
class Employee:
    _name = None

    def __new__(cls):
        if cls._name is None:
            print("Creating object using new")
            cls._name = super().__new__(cls)
            return cls._name
        else:
            raise Exception('class can have only one object')



obj1=Employee()
print(obj1)


#obj2=Employee()
#print(obj2)

"""

# lst = [2,3,6,6,5]
# new = set(lst)
# print(new)
# new_lst = list(new)
# max_item = max(new_lst)
# new_lst.remove(max_item)

# print(max(new_lst))

s = 'AAABCADDE'
k = 3

n = len(s)
var = int(n/k)

# a = s[0:var]
# print(a)
# x = var+var
# b = s[var:x]
# print(b)

# y = x+var
# c = s[x:y]
# print(c)

temp = 0
for i in range(0,var):
    sub = s[temp:var]
    temp = var
    var = temp+var
    print(sub)

    new = list(sub)
    new_d = set(new)
    print(new_d)

