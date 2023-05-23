# 9.      Write a program to sum the first 50 fibonacci sequence.
def fibonacci_sum(n):
    fibonacci_sequence = [0, 1]  #use the first 2 numbers to initialize
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    fibonacci_sum = sum(fibonacci_sequence[:n])
    return fibonacci_sum

# Calculate the sum of the first 50 Fibonacci numbers
n = 50
sum_of_fibonacci = fibonacci_sum(n)
print("Sum of the first", n, "Fibonacci numbers:", sum_of_fibonacci)