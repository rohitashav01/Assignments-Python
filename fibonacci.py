#Generating Fibonacci Series
def fib(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b= b,a+b

obj = fib(12)
print("fibonacci Series is :")
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))