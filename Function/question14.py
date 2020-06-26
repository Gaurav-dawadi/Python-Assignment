"""Write a Python program to sort a list of dictionaries using Lambda."""


dicList = [{'dog':'Tiger', 'color':'Gold'}, {'dog':'Panna', 'color':'White'}, {'dog':'Pintu', 'color':'Black'}]

sortedList = sorted(dicList, key = lambda dicList: dicList['color'])

print("The Sorted List is -> ", sortedList)