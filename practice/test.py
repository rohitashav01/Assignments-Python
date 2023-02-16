class Emp:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    def show(self):
        return f'Employee  first name {self.fname},employee last name {self.lname} and employee salary {self.salary}'
    
    def __add__(self,other):
        return self.salary + other.salary
    
    def __repr__(self):
        return f"{self.fname},{self.lname},{self.salary}"

if __name__ == '__main__':
    emp1=Emp("ravi","shastri",90000)
    emp2=Emp("himanshu","sharma",9)

    res=emp1.show()
    res2=emp2.show()
    print(res)
    print(res2)
    print(emp1)
    print(emp2)
    print(repr(emp1+emp2))
