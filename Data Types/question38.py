"""Write a Python program to remove a key from a dictionary."""


def removeItemOfDict(dic, inputKey):

    del dic[inputKey]
        # OR
    # dic.pop(inputKey)
    return dic


print(removeItemOfDict({1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, 4))
