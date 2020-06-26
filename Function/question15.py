"""Write a Python program to filter a list of integers using Lambda."""


inputList = [12, 6, 9, 18, 2, 4, 10, 25, 20, 16]

greaterThan = list(filter(lambda x: x>15, inputList))

print("Greater Than 15 Only ", greaterThan)