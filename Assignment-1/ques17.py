# Write a program in python that converts a given string to title case (first letter of each word capitalized).

def title_case(str):
    words = str.split()
    
    titled_words = [word.capitalize() for word in words]
    
    titled_str = ' '.join(titled_words)
    
    return titled_str

input_str = input("Enter a string: ")
title_string = title_case(input_str)

print(title_string)
