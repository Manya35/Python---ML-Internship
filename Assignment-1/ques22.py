# Write a python program that returns the minimum and maximum values in a list of numbers.

num = list(map(int, input("Enter numbers separated by spaces: ").split()))

max_num = max(num)
min_num = min(num)

print(f"The maximum value in the list is: {max_num}")
print(f"The minimum value in the list is: {min_num}")