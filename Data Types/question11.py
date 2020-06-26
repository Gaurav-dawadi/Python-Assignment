"""Write a Python program to count the occurrences of each word in a given
sentence."""

inputString = input("Enter a String: ")
newEmptyDict = {}

def occurenceOfWord(inputString):
    for char in inputString:
        if char in newEmptyDict:
            newEmptyDict[char] +=1
        else:
            newEmptyDict[char] = 1
     
    return newEmptyDict

print(occurenceOfWord(inputString))