"""Write a Python program to iterate over dictionaries using for loops."""

inputDict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

for k,v in inputDict.items():
    print(k, end='->')
    print(inputDict[k])