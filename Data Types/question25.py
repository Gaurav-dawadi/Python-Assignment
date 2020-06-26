"""Write a Python program to check whether all dictionaries in a list are empty or
not."""

def checkBool(inputList):   
    
    check = False

    for i in inputList:
        check += bool(i)
    return bool(check)     

print("List is Not Empty?", checkBool([{},{},{}]))
print("List is Not Empty?", checkBool([{1,2},{},{}]))

