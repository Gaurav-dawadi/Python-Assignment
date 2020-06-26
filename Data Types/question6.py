"""Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string."""

inputString = input("Enter a String: ")

def checkAndChange(inputString):
    findNot = inputString.find('not')          #Gives the index number of letter 'n' 
    findPoor = inputString.find('poor')        #Gives the index number of letter 'p'

    if findPoor > findNot and findNot>0 and findPoor>0:    #Checks if index of poor is greater than index of not and also both indexes are positive
        return inputString.replace(inputString[findNot:findPoor+4], 'good')
    else:
        return inputString    

result = checkAndChange(inputString) 
print(result)     

