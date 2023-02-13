#Bubble Sort to sort items in the list
lst = [12,98,87,44,50]

n = len(lst)
def bubble_sort(lst):
    for i in range(n):
        for j in range(n-i-1):
            if lst[j]> lst[j+1]:    
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp

    return lst

print(bubble_sort(lst))

