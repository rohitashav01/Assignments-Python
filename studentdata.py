#Operations on Student Data
lst = []
thisdict={
    "rollno":1,
    "name":"John",
    "subjects":["Hindi","English","Maths"],
    "class":11
}
lst.append(thisdict)
thisdict1={
    "rollno":2,
    "name":"Tim",
    "subjects":["Hindi","English","Maths"],
    "class":11
}
lst.append(thisdict1)
thisdict2={
    "rollno":3,
    "name":"Mathew",
    "subjects":["Hindi","English","Maths"],
    "class":11
}
lst.append(thisdict2)


#list_students

def list_students():
    name_lst=[]
    for i in lst:
        name_lst.append(i['name'])
    return name_lst

#search_students

def search_student():
    roll=int(input('Enter Roll No. to search student: '))
    for i in lst:
        if i['rollno']==roll:
           return i       
#update_student

def update_student():
    a=int(input("Enter roll no. to update the data of student: "))
    if(a==1):
        b=input("Enter the entity to update(name,subjects,class): ").lower()
        if(b=="name"):
            new_name=input("Enter Name for student: ")
            thisdict["name"]=new_name
        elif(b=="subjects"):
            new_sub=list(input("Enter Subjects for student: "))
            thisdict["subjects"]=new_sub
        elif(b=="class"):
            new_class=int(input("Enter Class for student: "))
            thisdict["class"]=new_class
        else:
            print("Enter a valid entity")
        return thisdict
    elif(a==2):
        b=input("Enter the entity to update(name,subjects,class): ").lower()
        if(b=="name"):
            new_name=input("Enter Name for student: ")
            thisdict1["name"]=new_name
        elif(b=="subjects" ):
            new_sub=list[input("Enter Subejcts for student: ")]
            thisdict1["subjects"]=new_sub
        elif(b=="class" ):
            new_class=int(input("Enter Class for student: "))
            thisdict1["class"]=new_class
        else:
            print("Enter a valid entity")
        return thisdict1
    elif(a==3):
        b=input("Enter the entity to update(name,subjects,class): ").lower()
        if(b=="name"):
            new_name=input("Enter Name for student: ")
            thisdict2["name"]=new_name
        elif(b=="subjects"):
            new_sub=list[input("Enter Subjects for student: ")]
            thisdict2["subjects"]=new_sub
        elif(b=="class" ):
            new_class=int(input("Enter Class for student: "))
            thisdict2["class"]=new_class
        else:
            print("Enter a valid entity")
        return thisdict2
    else:
        print("Enter a valid roll no.")

#delete_student

def delete_student():
    i=int(input("enter roll no. to delete the record of student: "))
    if(i==1):
        del lst[0]
        print("Record of roll no:1 deleted")
        return lst
    elif(i==2):
        del lst[1]
        print("Record of roll no:2 deleted")
        return lst
    elif():
        del lst[2]
        print("Record of roll no:3 deleted")
        return lst
    else:
        print("Enter a valid roll no.")
         

#add_student

def add_student():
    print("-----Enter record for a new student------")
    a=int(input('enter roll no: '))
    b=input("Enter Name")
    c=list[input('Enter subjects')]
    d=int(input("Enter Class: "))
    
    newdict={
        "roll no:":'',
        "name": " ",
        "subjects":'',
        "class": " "

    }

    newdict["roll no:"]=a
    newdict["name:"]=b
    newdict["subjects:"]=c
    newdict["class:"]=d
    lst.append(newdict)
    for i in lst:
        stud = i
    return stud
    

while True:
    
    print("1.List Students")
    print("2.Search Student")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Add Student")
    print("6.Exit")

    i=int(input("Choose Option: "))
    if(i==1):
        res=list_students()
        print(res)
    elif(i==2):
        res=search_student()
        print(res)
    elif(i==3):
        update_student()
    elif(i==4):
        res=delete_student()
        print(res)
    elif(i==5):
        res=add_student()
        print(res)
    else:
        break
   


