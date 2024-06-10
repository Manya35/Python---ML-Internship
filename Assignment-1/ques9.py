# Write a python program that checks if a substring is present in a given string.

str = input("Enter main string: ")

sub_str = input("Enter substring: ")

if sub_str in str:
    print(f"The substring ({sub_str} is present in the main string.)")
else:
    print(f"The substring ({sub_str} is not present in the main string.)")