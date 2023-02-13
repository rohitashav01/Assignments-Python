words = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',8:'eight',9:'nine', 10:'ten',
            11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',17:'seventeen',18:'eighteen', 19:'ninteen',
            20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty',70:'seventy',80:'eighty',90:'ninty', 100:'hundred', 1000:'thousand'
}
value=int(input("Enter number to convert into words[1-100]:  "))

def format(value):
    """
    Function is used to format the amount
    for example:
        30 --> 30.00
    param amount
    return
    """
    return f"{value}.00"

def convert(fun,amt):
    format_amount=fun(amt)
    format_amount=float(format_amount)

    if format_amount in words:
        result = words.get(format_amount)
    else:
        new = format_amount%10
        last_no= words.get(new)
        first=format_amount//10
        a=first*10
        first_no=words.get(a)
        result=first_no+" "+last_no
    return result

res = convert(format,value)
print(res)

