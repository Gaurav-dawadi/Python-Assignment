"""Write a Python program to insert a given string at the beginning of all items in
a list."""


def addString(inputList, inputString):

    newList =[inputString + str(i) for i in inputList]

    return newList    

print(addString([1,2,3,4], 'emp'))
print(addString([1,2,3,4], 'goal'))