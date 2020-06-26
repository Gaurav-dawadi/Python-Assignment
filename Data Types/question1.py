"""Write a Python program to count the number of characters (character
frequency) in a string."""


inputString = input("Enter a String:")

countedArray = {}

for char in inputString:
    if char in countedArray:  
        countedArray[char] += 1    
    else:
         countedArray[char] = 1
        
print(countedArray)     