
"""
def add(*args):
    print(*args)
    print(args)
    sum=0
    for arg in args:
        sum=sum+arg
    print(sum)
add(4,5)
        
def addition(**kwrgs):
    sum=0
    for val in kwrgs.values():
        sum=sum+val
    print(sum)
    for key,values in kwrgs.items():
        print(key,values)
    
addition(a=5,b=2,c=4,d=10)

"""

class Calculator:
    def calc(self,*args):
        sum=0
        for arg in args:
            sum=sum+arg
        print(sum)
        mul=1
        for arg in args:
            mul=mul*arg
        print(mul)
if __name__=='__main__':
    obj1=Calculator()
    obj1.calc(10,20,30,40,50)
    obj2=Calculator()
    obj2.calc(2,4,5)
    
	
class Student:
    def data(self, **kwargs):
        print(kwargs)
        for val in kwargs.values():
                print(val)
        for key,values in kwargs.items():
             print(key,values)
                
        #print(kwargs)
        #self.name = kwargs["name"]
        #self.age = kwargs["age"]
        #self.salary = kwargs["salary"]
	


st = Student()
st.data(name = 'John',age = 25, salary = 15000)
st2 = Student()
st2.data(name = 'Doe',age = 25,salary = 1500000)
