"""Write a Python function that accepts a string and calculate the number of
upper case letters and lower case letters."""


inputString = input("Enter a String: ")

upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCaseCount = 0
lowerCaseCount = 0
for i in inputString:  
        if i in upperCase:
            upperCaseCount += 1 
        elif i in lowerCase:
            lowerCaseCount += 1 

print("Total Uppercase: ", upperCaseCount)
print("Total Lowercase: ", lowerCaseCount)

