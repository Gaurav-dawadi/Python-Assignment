"""Write a Python program to unpack a tuple in several variables."""

inputTuples = (1,'gaurab','python',4)

x, *y, z = inputTuples

print(x)
print(*y)
print(z)