# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

conversion_type = input("Enter 'C to F' to convert Celsius to Fahrenheit or 'F to C' to convert Fahrenheit to Celsius: ").strip().upper()

if conversion_type == 'C TO F':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit}°F")
    
elif conversion_type == 'F TO C':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius}°C")
    
else:
    print("Invalid input. Please enter 'C to F' or 'F to C'.")

