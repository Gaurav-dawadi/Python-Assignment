"""Write a Python program to add an item in a tuple."""


"""Tuples are immutable so we cannot directly add or remove items from it. Therefore, converting Tuples to List"""

inputTuples = (1,'gaurab','python',4)

convertToList = list(inputTuples)

newList = convertToList.append('IW')

print(tuple(newList))