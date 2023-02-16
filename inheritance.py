"""
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

print("-------------------------------------------------------------------------------------------------------")

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

print("---------------------------------------------------------------------------------------------------------")


"""
"""
#Multilevel Inheritance


class Boy:
	def __init__(self,name,age):
         self.name=name
         self.age=age

	
class Father(Boy):
	def __init__(self,fname,name,age):
		self.fname=fname
		super().__init__(self,name,age)

	def age(self, a):
         print(f"Father Name: {self.fname},Son-Name:{self.name},Son-Age:{self.age}")
         print('Age of Father: ',a)       

class Mother(Father):
	def __init__(self,fname,name,age):
		print('Mother - Hii')
		super().__init__(self,fname,name,age)

	def age(self, a):
		print('Age of Mother: ', a)
		super().age(a - 5)

# Main function 
if __name__ == '__main__':
	obj = Mother("Raghuveer","Anuj",5)
	obj.age(30)

"""

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
