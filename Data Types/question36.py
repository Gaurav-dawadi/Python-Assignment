"""Write a Python program to sum all the items in a dictionary."""

def sumItemsOfDict(dic):
    sum = 0
    for items in dic:
        sum += dic[items]
    return sum

print("The sum of all items in dictionary: ", sumItemsOfDict({1: 10, 2: 20, 3: 30, 4: 40}))
