# linear Search 
lst = [85,34,42,89, 67]
print(lst)
search = int(input("Enter the no want to search: "))


#function to search a particular number
def linear_search(lst,x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

res = linear_search(lst,search)
if res == -1:
    print("Element not Found")
else:
    print("Element found at index:  ", res)
