"""Write a Python program to create a lambda function that adds 15 to a given
number passed in as an argument, also create a lambda function that multiplies
argument x with argument y and print the result."""


# inputNum = int(input("Enter a number: "))

print("The Result Of Addition is ", (lambda inputNum: inputNum + 15)(15))

print("The Result Of Multiplication is ",(lambda x,y:( x * y))(20, 25))
