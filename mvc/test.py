"""
Test Code for Practice

import csv
import os

def primary_key():
        roll_no = 0
        for i in range(1,10):
            # nonlocal roll_no
            roll_no += 1
        print(roll_no)



header = ['Primary Key','First Name','Last Name','email','phone number','uuid']
data = [{'Primary Key':1,'First Name':"rohit",'Last Name':'pathak','email':'abxc','phone number':12323,'uuid':219321},
        {'Primary Key':2,'First Name':"Abhishek",'Last Name':'Kumar','email':'xyzavc','phone number':99810239,'uuid':1010101}]

if os.path.isfile('C:/Users/rohitashav.pathak/Assignments-Python/mvc/test.csv'):
    with open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/test.csv', 'a', newline='') as my_file:
        w = csv.DictWriter(my_file, fieldnames = header)
        for row in data:
            w.writerow(row)
    
    for row in w:
        values = row[0]['Primary Key']
        print(values)
   
else:
    print('hello world')
    with open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/test.csv', 'w', newline='') as my_file:
        w = csv.DictWriter(my_file, fieldnames = header)
        w.writeheader()
        for row in data:
            w.writerow(row)

var = open('C:/Users/rohitashav.pathak/Assignments-Python/mvc/test.csv', 'r+', newline='')
w = csv.DictReader(var)
    #fieldnames = w.fieldnames
for rows in w:
    print(rows['Primary Key'])

"""