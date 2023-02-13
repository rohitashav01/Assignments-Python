#Finding the largest of three numbers

a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=int(input("Enter Third Number"))

if a>b:
    if a>c:
        print("The largest number is: " , a)
elif b>a:
    if b>c:
        print("The largest number is: " ,b)
else:
    print("The largest number is: ",c)

    
