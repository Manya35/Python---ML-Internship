# Write a program that takes a string input from the user and writes it to a text file.

user_input = input("Please enter a string: ")

file_name = "D:\Python & ML Internship\Assignment-1\text-file.txt"

with open(file_name, "w") as file:
    file.write(user_input)

print(f"The string has been written to {file_name}")