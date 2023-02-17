
#Single Inheritance1

class Parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f"Child is: {self.name}"
    def show(self):
        print("Name and age of your child is:",self.name,",", self.age) 

class Child(Parent):
    def __init__(self,address,name,age):
        self.address=address
        Parent.__init__(self,name,age)
        Parent.show(self)
        Parent.__repr__(self)
    def show_addr(self):
        return f'Address is: {self.address}'
        

if __name__=='__main__':
    raghu=Child("Chandigarh","Raghu",22)
    res=raghu.show_addr()
    
    print(res)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------")

#Single Inheritance 2


class Bank:
    def __init__(self,name,acc_no,bank_bal):
        self.name=name
        self.acc_no=acc_no
        self.bank_bal=bank_bal


    def show_details(self):
        print("Your account details: ","name: ",self.name,"Account Number: ",self.acc_no)
        

class Customer(Bank):
    def __init__(self,withdraw,rem_bal,name,acc_no,bank_bal):
        self.withdraw=withdraw
        self.rem_bal=rem_bal
        Bank.__init__(self,name,acc_no,bank_bal)
        self.rem_bal=self.bank_bal-self.withdraw
        Bank.show_details(self)

    def show_bal(self,): 
        return f"Your bank balance is: {self.bank_bal},Withdrawn Amount: {self.withdraw} and your remaining balance is: {self.rem_bal}"

if __name__=='__main__':
    cust1=Customer(25000,'',"Arun",199211001,100000)
    res=cust1.show_bal()
    print(res)

print("------------------------------------------------------------------------------------------------------------------------------------------------------")



#Multilevel Inheritance1


class Boy:
	def __init__(self,name,age):
         self.name=name
         self.age=age

	
class Father(Boy):
    def __init__(self,f_name,f_age,name,age):
        self.f_name=f_name
        self.f_age=f_age
        Boy.__init__(self,name,age)	

    def show(self):
        return f"Father Name: {self.f_name},Father-age:{self.f_age},Son-Name:{self.name},Son-Age:{self.age}" 

class Mother(Father):
    def __init__(self,f_name,f_age,name,age):
        Father.__init__(self,f_name,f_age,name,age)
        res=Father.show(self)
        print(res)
    
    def show_age(self):
        m_age=self.f_age-5
        return f"Age of mother is:{m_age}"

# Main function 
if __name__=='__main__':
    obj = Mother("Raghuveer",30,"Anuj",5)
    result=obj.show_age()
    print(result)

print("-----------------------------------------------------------------------------------------------------------------------------------")



#Multilevel Inheritance 2
class Bank:
    def __init__(self,name,acc_no,bank_bal):
        self.name=name
        self.acc_no=acc_no
        self.bank_bal=bank_bal


    def show_details(self):
        print("Your account details: ","name: ",self.name,"Account Number: ",self.acc_no)
        

class Customer(Bank):
    def __init__(self,withdraw,rem_bal,name,acc_no,bank_bal):
        self.withdraw=withdraw
        self.rem_bal=rem_bal
        Bank.__init__(self,name,acc_no,bank_bal)
        self.rem_bal=self.bank_bal-self.withdraw
        Bank.show_details(self)

    def show_bal(self): 
        return f"Your bank balance is: {self.bank_bal},Withdrawn Amount: {self.withdraw} and your remaining balance is: {self.rem_bal}"

class Loan(Customer):

    def __init__(self,loan,inters,withdraw,rem_bal,name,acc_no,bank_bal):
        self.loan=loan
        self.inters=inters
        Customer.__init__(self,withdraw,rem_bal,name,acc_no,bank_bal)
        res1=Customer.show_bal(self)
        print(res1)
              
    def loan_details(self):
        return f"You took a loan of {self.loan} at an interest rate of {self.inters}%"

if __name__=='__main__':
    cust1=Loan(2000000,12,25000,'',"Arun",199211001,100000)
    res=cust1.loan_details()
    print(res)

print("------------------------------------------------------------------------------------------------------------------------------------------------")



#Multiple Inheritance

class TeamMember:                   
   def __init__(self, name, uid): 
      self.name = name 
      self.uid = uid 
  
# Parent class 2
class Worker:                 
   def __init__(self, pay, jobtitle): 
      self.pay = pay 
      self.jobtitle = jobtitle 
  
# Deriving a child class from the two parent classes
class TeamLeader(TeamMember, Worker):         
   def __init__(self, name, uid, pay, jobtitle, exp): 
      self.exp = exp 
      TeamMember.__init__(self, name, uid) 
      Worker.__init__(self, pay, jobtitle)
      print("Name: {},ID: {}, Pay: {},Role:{}, Exp: {} years".format(self.name,self.uid, self.pay,self.jobtitle, self.exp))

TL = TeamLeader('Mark', 10001, 250000, 'Developer', 5)
