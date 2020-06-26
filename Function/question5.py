"""Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument."""

inputNumber = int(input("Enter a number: "))
fact = 1
for i in range(1, inputNumber+1):

    fact *= i 
print("The factorial is ", fact)     