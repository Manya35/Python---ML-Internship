#Write a program that reads the content of a text file and prints it to the console.

file_name = "D:\Python & ML Internship\Assignment-1\text-file.txt                                                "

with open(file_name, "r") as file:
    content = file.read()
    print("The content of the file is:")
    print(content)