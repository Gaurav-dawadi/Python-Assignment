"""Write a Python script to merge two Python dictionaries."""

def mergeDict(dic1, dic2):
    dic3 = {}
    for dic in (dic1, dic2):
        dic3.update(dic)
    return dic3

print(mergeDict({1:10, 2:20},{3:30, 4:40}))        