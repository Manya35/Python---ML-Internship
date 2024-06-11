# Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

string = input("Enter the string: ")

prefix = input("Enter the prefix: ").strip()
suffix = input("Enter the suffix: ").strip()

if prefix:
    print(f"String starts with '{prefix}': {string.startswith(prefix)}")

if suffix:
    print(f"String ends with '{suffix}': {string.endswith(suffix)}")
