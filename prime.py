# Program to find the prime number
start_no  = int(input("Enter number from which you want to find the Prime number :"))
end_no = int(input("Enter the number upto which you want to find the prime number: "))
res =[]
def prime(start_no, end_no):
    for num in range(start_no, end_no + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print("Prime numbers are:",num)
               
#Calling the Prime Function
prime(start_no, end_no)




