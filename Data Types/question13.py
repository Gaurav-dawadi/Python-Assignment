"""Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically)."""


inputNumber = int(input("Enter number of words you want in a sequence: "))

def sortWords(inputNumber):
   
    listOfWords = [input("Enter a single: ") for i in range(inputNumber)]

    print("-------------------------------------------------")
    print("Your Entered words are: ", ', '.join(listOfWords))
    print("-------------------------------------------------")
  
    return ', '.join(sorted(set(listOfWords)))

print("Your Result After Sorting is: ",sortWords(inputNumber))
print("-----------------------------------------------------")
