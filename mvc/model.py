import os
import csv
import uuid

def generate_uuid():
    return uuid.uuid4()

def primary_key(func):
        roll_no = 0
        def wrapper(*args, **kwargs):
            nonlocal roll_no
            roll_no += 1
            return func(*args,pk=roll_no)
        return wrapper



class Person(object):
    
    def __init__(self,first_name,last_name,email,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.uuid = generate_uuid()
    
    @primary_key
    def set_user(self,pk=None):
        header = ['Primary Key','First Name','Last Name','email','phone number','uuid']
        data = {'Primary Key':pk,'First Name':self.first_name,'Last Name':self.last_name,'email':self.email,'phone number':self.phone_number,'uuid':self.uuid}
        if os.path.isfile('user.csv'):
            with open('mvc/user.csv', 'a', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames = header)
                w.writerow(data)
        else:
            with open('mvc/user.csv', 'w', newline='') as my_file:
                    w = csv.DictWriter(my_file, fieldnames = header)
                    w.writeheader()
                    w.writerow(data)
    
    def initials(self):
        return self.first_name[0]+"."+self.last_name[0]

    @classmethod
    def getAllUser(cls):
        values = open('mvc/user.csv', 'r')
        result = []
        read = csv.DictReader(values)
        field = read.fieldnames
        for row in read:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result


class Blog(object):
    def __init__(self,date,topic):
        #self.user=user
        self.b_id = generate_uuid()
        self.date = date
        self.topic = topic
        #self.person = Person()
    
    def set_blog(self):
        header = ['ID','Date','Topic']
        data = {'ID':self.b_id,'Date':self.date,'Topic':self.topic}
        if os.path.isfile('blog.csv'):
            with open('mvc/blog.csv', 'a', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames= header)
                w.writerow(data)
        else:
            with open('mvc/blog.csv', 'w', newline='') as my_file:
                    w = csv.DictWriter(my_file, fieldnames = header)
                    w.writeheader()
                    w.writerow(data)
    
    @classmethod
    def getAllBlog(cls):
        values = open('mvc/blog.csv', 'r')
        result = []
        read = csv.DictReader(values)
        field = read.fieldnames
        for row in read:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result

