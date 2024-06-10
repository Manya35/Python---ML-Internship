# Write a python program that calculates the sum of the digits of a given number.

def sum_digits(n):
    num = str(abs(n))

    sum = 0

    for digit in num:
        sum += int(digit)
    
    return sum

num = int(input("Enter a number: "))

d_sum = sum_digits(num)

print(f"The sum of digits of {num} is: {d_sum}")