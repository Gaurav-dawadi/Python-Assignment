"""Write a Python program to replace the last element in a list with another list."""



def addListToList(list1, list2):

    return list1[0:-1] + list2[:]

print(addListToList([1, 3, 5, 7, 9, 10],[2, 4, 6, 8]))