"""Write a Python program to remove the characters which have odd index
values of a given string."""

inputString = input("Enter a String: ")

def removeOddIndexedChar(inputString):
    
    # newString = ""
    # for i in range(len(inputString)):
    #     if i%2 == 0:
    #         newString = newString + inputString[i]

    newString = [inputString[i] for i in range(len(inputString)) if i%2 == 0]        
    return ''.join(newString)

print(removeOddIndexedChar(inputString))          
