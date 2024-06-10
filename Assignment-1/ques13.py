# Write a program that asks the user for their birth year and calculates their age.

current_year = int(input("What year is it? "))
birth_year = int(input("Enter your birth year: "))

age = current_year - birth_year

print(f"You are {age} years old.")