"""Write a Python program to print the even numbers from a given list."""
      
def evenNumber(inputList):
    evenList = []

    for num in inputList:
        if num%2 == 0:
            evenList.append(num)
    
    return evenList        

print("The list of only even Numbers is ", evenNumber([1, 2, 3, 4, 5, 6, 7, 8, 9]))