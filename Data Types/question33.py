"""Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys"""

""" Same as that of Qeustion 32"""


inputDict = {}
for i in range(1, 16):
    inputDict[i] = i**2

print("The dictionary is: ", inputDict)