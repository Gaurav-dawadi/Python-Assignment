"""Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples."""

def getListOfTuples():
    takeList = []
    num = int(input("Enter number of tuples you want in list: "))
    
    for i in range(num):
        takeTuples = ()
        for j in range(2):
            inputElement = int(input("Enter an element for a tuple: "))
            takeTuples = takeTuples + (inputElement, )            
        takeList.append(takeTuples)
    print("---------------------------------------------------")
    print("The unsorted list of tuples is ",takeList)
    print("---------------------------------------------------")
    return takeList    

def getSortedList():
    unsortedList = getListOfTuples()

    sortedList = sorted(unsortedList, key = lambda tup: tup[1])
    return sortedList

print("The sorted List is ", getSortedList())
