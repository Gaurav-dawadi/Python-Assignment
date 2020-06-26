"""Write a Python function that takes a number as a parameter and check the
number is prime or not."""

inputNumber = int(input("Enter a Number: "))

def checkForPrime(inputNumber):
    count = 0
    for i in range(1, inputNumber+1):
        if inputNumber%i == 0:
           count += 1
    
    if count == 2:
        return "The Number is Prime"
    else:
        return "The Number is not Prime"
    
print(checkForPrime(inputNumber))       

