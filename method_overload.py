
"""
Practice code for args and kwargs
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
#method overloading 
#using args
class Calculator:
    """
    Class contains function calc
    to calculate sum and product of
    any number of arguments passed
    """
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

#Using args
class Calculate:
    """
    this class contains function 
    to calculte sum
    using any number of arguments
    atleast two arguments must be
    """
    def __init__(self,a,b,*args):
        self.a=a
        self.b=b
        sum=self.a+self.b
        for arg in args:
            sum=sum+arg
        print("Sum=",sum)
if __name__=='__main__':
    obj=Calculate(10,20,200,210)
    obj1=Calculate(20,30,40,50)


#Using **kwargs	
class Student:
    """
    Student class
    Displays student data
    Using keyword arguments
    
    """
    def data(self, **kwargs):
        print(kwargs)
        for val in kwargs.values():
                print(val)
        for key,values in kwargs.items():
             print(key,values)

if __name__=='__main__':
    st = Student()
    st.data(name = 'John',age = 25, salary = 15000,address='Chandigarh')
    st2 = Student()
    st2.data(name = 'Doe',age = 25,salary = 1500000)

