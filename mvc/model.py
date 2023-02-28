import os
import csv
import uuid

def generate_uuid():
    return uuid.uuid4()

def generate_pk():
        if os.path.isfile('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv'):
            var = open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv', 'r', newline='')
            w = csv.DictReader(var)
            for rows in w:
                pri_key = rows['Primary Key']
            new_pri=  int(pri_key)+1
            return new_pri
        else:
            print('File created')
            
# def generate_pk(func):
#     def wrapper(x):
#         if os.path.isfile('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv'):
#             var = open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv', 'r', newline='')
#             w = csv.DictReader(var)
#             for rows in w:
#                 pri_key = rows['Primary Key']
#             new_pri=  int(pri_key)+1
#             return new_pri
#         return func(x)     
#     return wrapper        

# def primary_key(func):
#     def wrapper(x):
#         print("hello world \n")
#         print(x.first_name)
#         return func(x)
#     return wrapper

class Person(object):
    def __init__(self,first_name,last_name,email,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.uuid = generate_uuid()
        self.pk = generate_pk()
    
    def set_user(self):
        header = ['Primary Key','First Name','Last Name','email','phone number','uuid']
        data = [{'Primary Key':self.pk,
                 'First Name':self.first_name,
                 'Last Name':self.last_name,
                 'email':self.email,
                 'phone number':self.phone_number,
                 'uuid':self.uuid}]
        if os.path.isfile('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv'):
            with open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv', 'a', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames = header)
                for row in data:
                    w.writerow(row)
        else:
            print('hello world')
            with open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv', 'w', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames = header)
                w.writeheader()
                data1 = [{'Primary Key':1,
                          'First Name':self.first_name,
                          'Last Name':self.last_name,
                          'email':self.email,
                          'phone number':self.phone_number,
                          'uuid':self.uuid}]
                for row in data1:
                    w.writerow(row)


    def initials(self):
        return self.first_name[0]+"."+self.last_name[0]

    @classmethod
    def getAllUser(cls):
        values = open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv', 'r')
        result = []
        read = csv.DictReader(values)
        field = read.fieldnames
        for row in read:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result

def read_pk():
    if os.path.isfile('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv'):
            blog = open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/user.csv', 'r', newline='')
            w = csv.DictReader(blog)
            for rows in w:
                pri_key = rows['Primary Key']
            return pri_key
           

class Blog(Person):
    def __init__(self,date,topic):
        self.b_pk = read_pk()
        self.b_id = generate_uuid()
        self.date = date
        self.topic = topic
    
    def set_blog(self):
        header = ['Primary Key','Date','Topic','ID']
        data = [{'Primary Key':self.b_pk,
                 'Date':self.date,
                 'Topic':self.topic,
                 'ID':self.b_id}]
        if os.path.isfile('C:/Users/rohitashav.pathak/Assignments-Python/mvc/blog.csv'):
            with open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/blog.csv', 'a', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames= header)
                for row in data:
                    w.writerow(row)
        else:
            with open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/blog.csv', 'w', newline='') as my_file:
                    w = csv.DictWriter(my_file, fieldnames = header)
                    w.writeheader()
                    # data1 = [{'Primary Key':1,
                    #           'Date':self.date,
                    #           'Topic':self.topic,
                    #           'ID':self.b_id}]
                    for row in data:
                        w.writerow(row)
    

    @classmethod
    def getAllBlog(cls):
        values = open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/blog.csv', 'r')
        result = []
        read = csv.DictReader(values)
        field = read.fieldnames
        for row in read:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result

