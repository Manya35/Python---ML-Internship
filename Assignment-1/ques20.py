# Write a python program that takes a list of numbers and returns their sum.

def sum_list(n):
    return sum(n)

num = list(map(int, input(f"Enter numbers separated by spaces: ").split()))

sum = sum_list(num)

print(f"The sum of list is: {sum}")
