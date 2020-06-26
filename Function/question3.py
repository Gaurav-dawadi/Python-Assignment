"""Write a Python function to multiply all the numbers in a list."""

def mulOfNumbersInList(inputList):
    
    mulOfItems = 1

    for items in inputList:
        mulOfItems *= items

    return mulOfItems

print(mulOfNumbersInList([8, 2, 3, -1, 7]))        