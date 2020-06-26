"""Write a Python program to check whether a given string is number or not
using Lambda."""


inputString = input("Enter a String: ")

stringNum = (lambda x : x.isdigit())

print("Is Number? -> ", stringNum(inputString))