"""Write a Python program to add 'ing' at the end of a given string (length should
be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
string length of the given string is less than 3, leave it unchanged."""

inputString = input("Enter a String: ")

def changeString(inputString):
    if len(inputString) >=3 : 
        checkEnteredString = inputString[-3:]

        if checkEnteredString != 'ing':
            return inputString[:] + 'ing'
        elif checkEnteredString == 'ing':
            return inputString + 'ly'  
    else: 
        return inputString

result = changeString(inputString)
print(result)       