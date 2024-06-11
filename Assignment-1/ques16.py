# Write a program in python that counts the frequency of each character in a string.

def count_freq(str):
    dict = {}

    for char in str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    
    return dict

input_str = input("Enter a string: ")

freq = count_freq(input_str)

for char, char_freq in freq.items():
    print(f"'{char}' : {char_freq}")