"""Write a Python program to clone or copy a list."""



inputNum = int(input("Enter number of items to be in list: "))

list1 = [int(input("Enter item in List: ")) for i in range(inputNum)]

list2 = list1.copy()

print(list2)