# Write a python program that counts the occurrences of a specific element in a list.

def count(i, lst):
    return lst.count(i)

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
num = int(input("Enter the element to count: "))
occurrences = count(num, lst)

print(f"The element {num} occurs {occurrences} times in the list.")
