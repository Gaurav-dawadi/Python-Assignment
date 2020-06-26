"""Write a Python program to square and cube every number in a given list of
integers using Lambda."""


inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newList = []
# def squareList(inputList):
#     for items in inputList:
#         listSquare = items**2
#         newList.append(listSquare)
#     return newList
# print(squareList(inputList))

print("The Square Of List is -> ", list(map(lambda inputList: inputList**2, inputList)))

print("The Cube Of List is -> ", list(map(lambda inputList: inputList**3, inputList)))

