
#OOPS Classes Examples

#Class1
class Vehicle:
    doors=5
    wheels=4
    distance=0
    speed=0
    def car(self):
        print("Car with four wheels and five doors is jimny")
    #Calculating Speed of Vehicle
    def time(self):
        time_taken=self.distance//self.speed
        return time_taken
    
model=Vehicle()
print("Accessing data members using object: ")
print("No. of wheels in the car are: ",model.wheels)
print("No. of doors in the car are: ",model.doors)
print("Accessing function using object: ")
model.car()
model.distance=240
model.speed=40
print("Speed of car in km/hrs: ",model.speed)
print("Distance covered by car in kms: ",model.distance)
print("Time taken by car in hrs: ",model.time())
print("--------------------------------------------------------------------------------------------------------")


#Class2
class Employee:
    e_id=0
    e_name=''
    e_dept=''
    #Defining Identification of Employee
    def identify(self):
        return f'Employee with Employee ID {self.e_id},is{self.e_name},and  working in the department:  {self.e_dept}'
#employee1
emp1=Employee()
#employee 2
emp2=Employee()
emp1.e_id=1
emp1.e_name='Rajesh'
emp1.e_dept='Testing'
emp2.e_id=2
emp2.e_name='Saurav'
emp2.e_dept='Designing'
res=Employee.identify(emp1)
print(res)
res1=Employee.identify(emp2)
print(res1)

print("----------------------------------------------------------------------------------------------------------")


#Class3
class Calc:
    length=0
    breadth=0
    height=0
    def volume(self):
        return self.length*self.breadth*self.height

cal=Calc()
cal.length=10
cal.breadth=20
cal.height=30
print("Length: ",cal.length)
print("Breadth: ",cal.breadth)
print("Height: ",cal.height)
print("Volume: ")
res= cal.volume()
print(res)
print("-----------------------------------------------------------------------------------------------------------")

#Class4
class Channel:
    time= ''
    name=""
    anchors=""
    #display channel information
    def disp_news(self):
        return f'The name of Channel is: {self.name} and it broadcasts at: {self.time} AM with anchor {self.anchors}'

ch1 = Channel()
ch1.time=9
ch1.name= "Metro News One"
ch1.anchors="Robin"
res = ch1.disp_news()
print(res)


print("-------------------------------------------------------------------------------------------------------")


#Class5
class Room:
    length = 0.0
    breadth = 0.0
    
    #calculate area
    def calculate_area(self):
        return self.length*self.breadth


study_room = Room()
study_room.length = 82.5
study_room.breadth = 79.2
print("Length: ",study_room.length)
print("Breadth: ",study_room.breadth)

print("Area: ",study_room.calculate_area())


print("-----------------------------------------------------------------------------------------------------------------")