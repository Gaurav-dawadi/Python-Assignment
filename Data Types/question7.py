"""Write a Python function that takes a list of words and returns the length of the
longest one."""

numberOfWordsInList = int(input("Enter number of words to be List: "))

def longestWordInList(numberOfWordsInListt):

    createdList = [input("Enter any word: ") for i in range(numberOfWordsInList)]    

    lengthOfItems = [(len(items), items) for items in createdList]

    return max(lengthOfItems)


print(longestWordInList(numberOfWordsInList))
