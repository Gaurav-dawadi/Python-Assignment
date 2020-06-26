"""Write a Python function that takes a list and returns a new list with unique
elements of the first list."""


def uniqueElementOnly(inputList):

    uniqueSelection = set(inputList)

    return list(uniqueSelection)

print(uniqueElementOnly([1,2,3,3,3,3,4,5]))
