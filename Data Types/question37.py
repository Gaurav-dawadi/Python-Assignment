"""Write a Python program to multiply all the items in a dictionary."""

def mulItemsOfDict(dic):
    mul = 1
    for items in dic:
        mul *= dic[items]
    return mul

print("The multiplication of all items in dictionary: ", mulItemsOfDict({1: 10, 2: 20, 3: 30, 4: 40}))