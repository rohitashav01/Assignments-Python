import datetime
#import re
import maskpass
import base64

stud_data=[]

#Email Validation    
def email_validation(func):
    
    def inner(stud_fname,stud_lname,stud_subs,stud_class,stud_email,*args,**kwargs):
        print(stud_email)
        if not "@" in stud_email:
            print("Invalid email")
            raise Exception("Invalid Email")
        elif not stud_email[-4:] in ".com.org.edu.gov.net":
            print(stud_email[-4:])
            print("Invalid email2")
            raise Exception("Invalid Email")
        return func(stud_fname,stud_lname,stud_subs,stud_class,stud_email,*args,**kwargs)
    return inner

#Password Validation

def is_password_valid(min_length):
    def inner(func):
            def sub_inner(stud_fname,stud_lname,stud_subs,stud_class,stud_email,passwd,*args,**kwargs):
                
                #encpwd = base64.b64encode(passwd.encode("utf-8"))
                spcChar =['$', '@', '#', '%','*','^','(',')']
                val = True
                
                if len(passwd) < min_length:
                    print('length should be at least 6')
                    val = False
                    
                if len(passwd) > 20:
                    print('length should be not be greater than 8')
                    val = False
                    
                if not any(char.isdigit() for char in passwd):
                    print('Password should have at least one numeral')
                    val = False
                    
                if not any(char.isupper() for char in passwd):
                    print('Password should have at least one uppercase letter')
                    val = False
                    
                if not any(char.islower() for char in passwd):
                    print('Password should have at least one lowercase letter')
                    val  = False
                    
                if not any(char in spcChar for char in passwd):
                    print('Password should have at least one of the symbols $@#%*^()')
                    val = False
                if val:
                    return val
                return func(stud_fname,stud_lname,stud_subs,stud_class,stud_email,passwd,*args,**kwargs)
            return sub_inner
    return inner
    
@email_validation
@is_password_valid(min_length=6)
def stud_register(stud_fname,stud_lname,stud_subs,stud_class,stud_email,passwd,stud_bdate):

    
    stud_ind_data= {
        "fname":'',
        "lname":'',
        "subjects":'',
        "class":'',
        "dob":'',
        "age":'',
        "email":'',
        "password":''

    }

    #DOB Validation
    
    day, month, year = map(int,stud_bdate.split('/'))
    birth_date = datetime.date(year, month, day)
    current_year = datetime.datetime.now().year
    current_month=datetime.datetime.now().month
    if year>current_year and month>current_month:
        print("Birthdate Invalid")

    # current age based on entered DOB  
    age = current_year - birth_date.year
    print(age)

    stud_ind_data["fname"]=stud_fname
    stud_ind_data["lname"]=stud_lname
    stud_ind_data["subjects"]=stud_subs
    stud_ind_data["class"]=stud_class
    stud_ind_data["dob"]=stud_bdate
    stud_ind_data["age"]=stud_bdate
    stud_ind_data["email"]=stud_email
    stud_ind_data["password"]=passwd
    stud_data.append(stud_ind_data)
    res = stud_data
    print(res)


    
#Login Function
def login():
    inp_email=input("Enter your email:").strip()
    inp_passwd=maskpass.askpass(prompt="Enter Your Password" ,mask="*")
    
    for i in stud_data:
        if inp_email==i['email'] and inp_passwd==i['password']:
            #if email and password matches with existing email and password
            print("Login Successful")
            def update_details():
                #updating the student details
                stud_attr=input("Enter the attribute to update(fname,lname,subjects,class): ").lower()
                if stud_attr=="fname":
                    new_fname=input("Enter New First Name for student: ")
                    i["fname"]=new_fname
                if stud_attr=="lname":
                    new_lname=input("Enter New First Name for student: ")
                    i["lname"]=new_lname
                elif stud_attr=="subjects":
                    new_sub=list[input("Enter Subjects for student: ")]
                    i["subjects"]=new_sub
                elif stud_attr=="class":
                    new_class=int(input("Enter Class for student: "))
                    i["class"]=new_class
                else:
                    print("Enter a valid entity")
                return stud_data
            def delete_student():
                    del stud_data[i]
                    return stud_data
            
            while True:
                print("1.Update Details")
                print("2.Delete Details")
                print("3.Exit")

                inp=int(input('Choose Option: '))
                if inp==1:
                    result=update_details()
                    print(result)
                elif inp==2:
                    result=delete_student()
                    print(result)
                elif inp==3:
                    exit()
                else:
                    print("Choose a Valid Option")
        else:
            print("Wrong Credentials or Register Yourself First")
    
    



while True:
    print("1.Log In: ")
    print("2.Register as a new student: ")

    i=int(input("Choose Option: "))
    if i==1:
        res=login()
        print(res)
    elif i==2:
        stud_fname=input("Enter First Name: ")
        stud_lname=input("Enter Last Name: ")
        stud_subs=list[input("Enter your Subjects: ")]
        stud_class=int(input("Enter Class of student: "))
        stud_email=input("Enter your email: ")
        passwd=maskpass.askpass(prompt="Enter Password" ,mask="*")
        stud_bdate = input("Type your Date of birth (ie.10/11/2011) : ")
        res=stud_register(stud_fname,stud_lname,stud_subs,stud_class,stud_email,passwd,stud_bdate)
        print(res)
