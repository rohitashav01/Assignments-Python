
class Emp:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    def show(self):
        return f'Employee  first name {self.fname},employee last name {self.lname} and employee salary {self.salary}'
    
    def __add__(self,other):
        return self.salary + other.salary
        
    #gives developer friendly output
    def __repr__(self):
        return f"{self.fname},{self.lname},{self.salary}"
        
    #gives the user friendly output
    def __str__(self):
        return f"This  represents objects for: {self.fname}"
    
    def __call__(self):
        print("Object is called using call method")
      

if __name__ == '__main__':
    emp1=Emp("ravi","shastri",90000)
    emp2=Emp("himanshu","sharma",9999)

    res=emp1.show()
    res2=emp2.show()
    print(res)
    print(res2)
    print(emp1)
    print(emp2)
    print(repr(emp1))
    print(repr(emp2))
    print(emp1+emp2)
    emp1()
    emp2()
"""
class Math:

    class Math
    Calculate circle area and circumference

    
    PI=3.14
    def __init__(self,radius):
        self.radius=radius
    
    def calculate_area(self):
        return Math.PI*self.radius*self.radius

    def circumference_of_cir(self):
        return 2*self.PI*self.radius
if __name__=='__main__':
    circle=Math(20)
    print(circle.calculate_area())
    circle.PI=3.141592653589793238
    print(circle.circumference_of_cir())


"""