"""Write a Python program to find intersection of two given arrays using
Lambda."""

array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [1, 2, 5, 6, 10, 12, 15, 19]

commonInArrays = list(filter(lambda x : x in array1, array2))

print("Intersection of two given arrays is  --> ", commonInArrays)
