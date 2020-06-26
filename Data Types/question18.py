"""Write a Python program to get the largest number from a list."""


inputNumberOfList = int(input("Enter number of items to be in List: "))

def largestInList(inputNumberOfList):   

    inputList = [int(input("Enter a number in List: ")) for num in range(inputNumberOfList)] 

    maxNumber = max(inputList)

    return maxNumber

print("The largest number from a list: ", largestInList(inputNumberOfList))