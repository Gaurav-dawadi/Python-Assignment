"""Write a Python program to change a given string to a new string where the first
and last chars have been exchanged."""


inputString = input("Enter a String: ")

def exchangeFirstAndLastChar(inputString):
    firstChar = inputString[0]
    lastChar = inputString[-1]

    newString = lastChar + inputString[1:-1] + firstChar

    return newString

print(exchangeFirstAndLastChar(inputString))    