"""Write a Python script that takes input from the user and displays that input
back in upper and lower cases."""


takeInput = input("Enter any word: ")

upperCase = takeInput.upper()
lowerCase = takeInput.lower()

print("All UpperCase: ", upperCase)
print("All LowerCase: ", lowerCase)