# Write a python program that generates the first n numbers in the Fibonacci sequence.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_seq = [0,1] 
    while len(fib_seq) < n:
        next = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next)
    
    return fib_seq

x = int(input("Enter a number: "))

fibonacci_sequence = fibonacci(x)

print(f"The first {x} numbers in fibonacci sequence are: {fibonacci_sequence}")