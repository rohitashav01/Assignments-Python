
#OOPS Classes Examples

#Class1
class Vehicle:
    def __init__(self,doors,wheels,distance,speed):
        self.doors=doors
        self.wheels=wheels
        self.distance=distance
        self.speed=speed
    def car(self):
        print(f"Car with {self.wheels}  wheels and {self.doors} doors is jimny")
    #Calculating Speed of Vehicle
    def time(self):
        time_taken=self.distance//self.speed
        return time_taken
if __name__=='__main__':  
    model=Vehicle(5,4,240,40)
    print("Accessing data members using object: ")
    print("No. of wheels in the car are: ",model.wheels)
    print("No. of doors in the car are: ",model.doors)
    print("Accessing function using object: ")
    model.car()
    print("Speed of car in km/hrs: ",model.speed)
    print("Distance covered by car in kms: ",model.distance)
    print("Time taken by car in hrs: ",model.time())
print("--------------------------------------------------------------------------------------------------------")


#Class2
class Employee:
    def __init__(self,e_id,e_name,e_dept):
        self.e_id=e_id
        self.e_name=e_name
        self.e_dept=e_dept
    #Defining Identification of Employee
    def identify(self):
        return f'Employee with Employee ID {self.e_id} is{self.e_name} and  working in the department:  {self.e_dept}'

if __name__=='__main__':
    #employee1
    emp1=Employee(1,"Rajesh","Testing")
    #employee 2
    emp2=Employee(2,"Saurav","Designing")
    print(Employee.identify(emp1))
    print(Employee.identify(emp2))
print("----------------------------------------------------------------------------------------------------------")


#Class3
class Calc:
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height
    def volume(self):
        return self.length*self.breadth*self.height

if __name__=='__main__':
    obj1=Calc(10,20,30)
    obj2=Calc(20,30,40)

    print("Volume: ")
    print(Calc.volume(obj1))
    print(Calc.volume(obj2))
print("-----------------------------------------------------------------------------------------------------------")

#Class4
class Channel:
    
    def __init__(self,time,name,anchors):
        self.time=time
        self.name=name
        self.anchors=anchors
    #display channel information
    def disp_news(self):
        return f'The name of Channel is: {self.name} and it broadcasts at: {self.time} AM with anchor {self.anchors}'
if __name__=='__main__':
    ch1 = Channel(9,"Metro News One","Robin")
    ch2=Channel(11,"Metro News One","Dony")
    res = ch1.disp_news()
    print(res)
    res1=ch2.disp_news()
    print(res1)


print("---------------------------------------------------------------------------------------------------------------")


#Class5
class Room:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    #calculate area
    def calculate_area(self):
        return self.length*self.breadth

if __name__=='__main__':
    study_room = Room(35,40)
    study_room2 = Room(45,80)

    print("Length for first room: ",study_room.length)
    print("Breadth for first room: ",study_room.breadth)

    print("Area: ",study_room.calculate_area())

    print("Length for second room: ",study_room2.length)
    print("Breadth for second room: ",study_room2.breadth)
    print("Area: ",study_room2.calculate_area())


print("-----------------------------------------------------------------------------------------------------------------")