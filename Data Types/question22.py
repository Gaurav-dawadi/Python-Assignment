"""Write a Python program to remove duplicates from a list."""

inputNum = int(input("Enter number of items to be in list: "))
inputUniqueList = []

def removeDuplicates(inputNum): 

    inputList = [int(input("Enter numbers as List items: ")) for i in range(inputNum)]      

    for num in inputList:
        if num not in inputUniqueList:
            inputUniqueList.append(num)
    return inputUniqueList
   
    """ another easy method is use of set(): 
            noDuplicates = set(inputList)
            return list(noDuplicates)"""

print(removeDuplicates(inputNum))

