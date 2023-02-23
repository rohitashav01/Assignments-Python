from model import Person
from model import Blog

#User Data
def startView():
   print('Do you want enter the data?[y/n]')


def enterInput():
   fname=input("Enter First Name: ")
   lname=input("enter Last name: ")
   mail=input("enter mail: ")
   number=int(input("Enter Number: "))
   obj = Person(first_name=fname,last_name=lname,email=mail,phone_number=number)
   obj.set_user()
   return obj

def showAllView(list):
   print('In our db we have %i users. Here they are:' % len(list))
   for item in list:
      print(item)

def showView():
    print("Do you want to see the User Data(y/n)?")

#Blog Data

def enterBlog():
   print("Do you want to enter the blog data?(y/n)")

def inputBlog():
   
   bdate=input("Enter Date of Release: ")
   btopic=input("Enter Topic of Blog: ")
   #buser= showInput()
   obj2 = Blog(date = bdate,topic=btopic)
   obj2.set_blog()

def showAllBlog(list):
   print('We have %i blogs' % len(list))
   for i in list:
      print(i)

def seeBlog():
   print("Do you want to see the Blog Data")


def endView():
   print('Goodbye!')
            
