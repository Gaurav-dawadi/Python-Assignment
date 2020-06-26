"""Write a Python program to get a single string from two given strings, separated
by a space and swap the first two characters of each string."""

inputFirstString = input("Enter first String: ")
inputSecondString = input("Enter second String: ")

def extractDigitsAndSwap(inputFirstString, inputSecondString):
    char1 = inputFirstString[0:2]
    char2 = inputSecondString[0:2]

    return char2 + inputFirstString[2:] + ' ' + char1 + inputSecondString[2:]


result = extractDigitsAndSwap(inputFirstString, inputSecondString)
print(result)