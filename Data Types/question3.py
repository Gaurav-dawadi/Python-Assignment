"""Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself."""

inputString = input("Enter a String: ")

def changeCharToDollor(inputString):
    char = inputString[0]
    inputString = inputString.replace(char, '$')
    return char + inputString[1:]

    # for i in range(1, len(inputString)+1):
    #     if inputString[i] == char:
    #         return inputString[0:i] + '$' + inputString[i+1: ]

result = changeCharToDollor(inputString)
print(result)