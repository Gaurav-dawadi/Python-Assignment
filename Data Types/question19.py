"""Write a Python program to get the smallest number from a list."""

inputNumberOfList = int(input("Enter number of items to be in List: "))

def smallestInList(inputNumberOfList):   

    inputList = [int(input("Enter a number in List: ")) for num in range(inputNumberOfList)] 

    minNumber = min(inputList)

    return minNumber

print("The smallest number from a list: ", smallestInList(inputNumberOfList))