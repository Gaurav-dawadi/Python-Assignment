"""Write a Python script to check whether a given key already exists in a
dictionary."""


def checkKeyInDict(inputDict, inputKey):
    if inputKey in inputDict:
        return ("Key already exist")
    else:
        return ("Key doesnot exist")    

print(checkKeyInDict({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 4))