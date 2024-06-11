# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operator. Please use one of +, -, *, /."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /): ").strip()

result = calculator(num1, num2, operator)

print(f"The result of {num1} {operator} {num2} is: {result}")
