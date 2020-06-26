"""Write a Python function to create the HTML string with tags around the
word(s)."""

value = input("Enter a word: ")
tag = input("Enter any HTML tag: ")

def createHTML(value, tag):
    return '<%s>%s<%s>' % (tag, value, tag)

print(createHTML(value, tag))


    