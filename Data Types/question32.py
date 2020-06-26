"""Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x)."""

n = int(input("Enter any number: "))
inputDict = {}
for i in range(1, n+1):
    inputDict[i] = i**2

print("The dictionary is: ", inputDict)
