"""Write a Python function to check whether a number is in a given range."""

inputNum = int(input("Enter a number: "))
inputLower = int(input("Enter lower value of Range: "))
inputHigher = int(input("Enter higher value of Range: "))

def checkNum(inputLower, inputHigher):

    if inputNum in range(inputLower, inputHigher):
        return ("A number is in a given range")
    else:
        return ("A number isnot in a given range")       

print(checkNum(inputLower, inputHigher))
