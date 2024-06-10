# Write a python program that calculates the factorial of a given number.

def factorial(n):
    if n==0 or n==1 :
        return 1
    else:
        return n * factorial(n-1)

x = int(input("Enter a number: "))
print(f"The factorial of {x} is: {factorial(x)}")