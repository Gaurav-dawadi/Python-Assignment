"""Write a Python program to sort a list of tuples using Lambda."""


listOfTuples = [('cat', 2), ('bat', 6), ('rat', 10), ('mat', 4)]

sortedList = sorted(listOfTuples, key=lambda listOfTuples: listOfTuples[1])

print("The Sorted List is -> ", sortedList)
