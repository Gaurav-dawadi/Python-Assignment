"""Write a Python program to check a list is empty or not."""

list1 = []
inputNum = int(input("Enter number of items to be in list: "))


list2 = [int(input("Enter item in List: ")) for i in range(inputNum)]
print("--------------------------------")

if list2 == list1:
    print("The list is empty")
else:
    print("The list is not empty")    