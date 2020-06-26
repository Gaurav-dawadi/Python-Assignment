"""Write a Python function to insert a string in the middle of a string."""

inputString = input("Enter any String/symbols: ")
inputWord = input("Enter any word: ")

def insertStringInString(inputString, inputWord):
    lengthOfString = len(inputString)
    return inputString[0:(lengthOfString//2)] + inputWord + inputString[(lengthOfString//2):]

print(insertStringInString(inputString, inputWord))    
