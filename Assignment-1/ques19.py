#  Write a python program that removes all punctuation from a given string.

str = input("Enter string: ")

print(f"The original string is: {str}")

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for i in str:
    if i in punc:
        str = str.replace(i, "")

print(f"The string after punctuation filter: {str}")