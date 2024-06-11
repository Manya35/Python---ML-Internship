# Write a python program that checks if two strings are anagrams of each other.

def anagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

str1 = input("Enter one string: ")
str2 = input("Enter another string: ")

if anagrams(str1,str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not amagrams.")