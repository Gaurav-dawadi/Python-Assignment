"""Write a Python program to multiplies all the items in a list."""


inputNumberOfList = int(input("Enter number of items to be in List: "))

def multiplicationOfItems(inputNumberOfList):   
    totalMultiplication = 1

    inputList = [int(input("Enter a number in List: ")) for num in range(inputNumberOfList)]    

    for items in inputList:
        totalMultiplication *= items

    return totalMultiplication    

print("The Total Multiplication Of Items: ", multiplicationOfItems(inputNumberOfList))
