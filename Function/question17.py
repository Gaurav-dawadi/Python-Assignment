"""Write a Python program to find if a given string starts with a given character
using Lambda."""


# def startWith(inputString, inputChar):

#     if inputString.startswith(inputChar):
#         return True
#     else:
#         return False

# print(startWith("How are You?", "H"))


stringStartsWith = (lambda x : True if x.startswith('H') else False)

print(stringStartsWith('How are You?'))