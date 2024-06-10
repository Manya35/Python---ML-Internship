# Write a python program that checks whether a given number is even or odd.

def is_even(n):
    return n % 2 == 0

x = int(input("Enter a number: "))

if is_even(x):
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")