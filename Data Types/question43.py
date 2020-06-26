"""Write a Python program to remove an item from a tuple."""


"""Tuples are immutable so we cannot directly add or remove items from it. Therefore, converting Tuples to List"""

inputTuples = (1,'gaurab','python',4)

convertToList = list(inputTuples)

newList = convertToList[0:2] + convertToList[3:]

print(tuple(newList))