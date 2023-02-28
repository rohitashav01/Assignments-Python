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

# a = 'abc'
# #returns true or false whether the string contains the specified argument
# #print(dir(a))
# hash_value = hash(a)
# print(hash_value)
# print(a.__contains__('d'))

# #print(a.__doc__)
# # class Human():
# #     def __init__(self):
# #         pass
# #     def age(self):
# #         print("age=20")

# # a = Human()
# # a.age()
# # print(a.__doc__)

# # eq --> Used to equate two objects
# # gt --> greater than -- used to compare two objects
# # ge --> greater than or equal to
# # hash --> used to return the hash value of an object

# class Person:

#     def __init__(self, first_name, last_name, age, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.salary = salary

#     def __eq__(self, other):
#         return self.age == other.age
    
#     def __gt__(self,other):
#         return self.salary > other.salary
    
# john = Person('John', 'Doe', 25,30000)
# jane = Person('Jane', 'Doe', 27,29000)
# x = Person.__delattr__(john.age)
# print(john)
# print(john == jane)  # True
# print(john > jane)
# #format --> 
# x = 32
# print(format(x,'f'))

# #iter
# lst = ['a','b','c','d','e','f']
# iter_list = iter(lst)
# #print(dir(lst))

# print(next(iter_list))
# print(next(iter_list))

# # format_map : used to return a dictionary's key value

# a = {'x':'John', 'y':'Wick'}
# print("{x}'s last name is {y}".format_map(a))
# print("{} oseof {}".format(a))

# tup = ('hello','world')
# print(dir(tup))
# print((1).__ne__(2))


# lst = [1,2,3,4,5]

# a = [x for x in lst if x%2==0]
# print(a)




# a = '123456789'

# b = a[0]
# c = a[-1]
# d = ''
# e = a[1:-1]
# print(c+e+b)

# #output : 923456781


# n=10
# for i in range(1, 6):
#     print(' '*n, end='') # repet space for n times
#     print('* '*(i)) # repeat stars for i times
#     n-=1