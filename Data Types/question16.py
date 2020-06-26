"""Write a Python program to sum all the items in a list."""

inputNumberOfList = int(input("Enter number of items to be in List: "))

def sumOfItems(inputNumberOfList):   

    inputList = [int(input("Enter a number in List: ")) for num in range(inputNumberOfList)]

    totalSum = sum(inputList)   
    return totalSum  

print("The Total Sum Of Items: ",sumOfItems(inputNumberOfList))

