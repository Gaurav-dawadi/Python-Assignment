"""Write a Python program to create a function that takes one argument, and
that argument will be multiplied with an unknown given number."""

"""If unknown number is any randomly generated number then"""

import random

inputNum = int(input("Enter a number: "))

def performMul(inputNum):

    unknownNumber = random.randint(0, 100) 
    print("---------------------------------")
    print("Unknown Number is ", unknownNumber) 
    print("---------------------------------") 

    return inputNum * unknownNumber

print(performMul(inputNum))










