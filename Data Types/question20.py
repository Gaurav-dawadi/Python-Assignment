"""Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings."""

inputNumberOfList = int(input("Enter number of items to be in List: "))

def countSameItemsInList(inputNumberOfList):   
    count = 0
    inputList = [(input("Enter a items in List: ")) for num in range(inputNumberOfList)]

    print("--------------------------------------------------------------")
    
    for items in inputList:
        if len(items) >= 2 and items[0] == items[-1]:
            count += 1

    return count


print("The total count is ", countSameItemsInList(inputNumberOfList))    