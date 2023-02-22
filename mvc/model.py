import random
import csv

def generate_uuid():
        return random.randint(0,10000)

class Person(object):
    
    def __init__(self,first_name,last_name,email,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.uuid = generate_uuid()
    
    
    def set_user(self):
        header = ['First Name','last_name','email','phone_number','uuid']
        with open('mvc/user.csv','w+',encoding='UTF8',newline='') as f:
            print('hello world')
            writer = csv.writer(f)
            writer.writerow(header)
    
        data = [self.first_name,self.last_name,self.email,self.phone_number,self.uuid]
        with open('mvc/user.csv','a+',encoding='UTF8',newline='') as f:
            print('hello world')
            writer = csv.writer(f)
            writer.writerow(data)
        

    def initials(self):
        return self.first_name[0]+"."+self.last_name[0]
    
  


"""  
    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getAll(cls):
        database = open('grades.csv', 'r')
        result = []
        reader = csv.DictReader(database)
        field = reader.fieldnames
        for row in reader:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result

"""
fname=input("Enter First Name: ")
lname=input("enter Last name")
mail=input("enter mail")
number=int(input("Enter Number:"))
obj = Person(first_name=fname,last_name=lname,email=mail,phone_number=number)
obj.set_user()

"""
header = ['Name','area','country_code','Geographical Location']

data = ['India',44550,'IND','North of Equator']

with open('mvc\countries.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

"""