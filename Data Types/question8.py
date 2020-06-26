"""Write a Python program to remove the nth index character from a nonempty
string."""

inputString = input("Enter a String: ")

inputIndex = int(input("Enter the index you want character to be poped from: "))

resultedString = inputString[0:inputIndex] + inputString[inputIndex+1:]

print(resultedString)