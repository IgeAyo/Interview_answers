#8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10
import random

def generate_random_binary():
    binary_digits = [str(random.randint(0, 1)) for _ in range(4)]
    binary_string = "".join(binary_digits)
    return binary_string

def convert_binary_to_decimal(binary_string):
    decimal = int(binary_string, 2)
    return decimal

# Generate a random binary number
random_binary = generate_random_binary()
print("Random Binary Number:", random_binary)

# Convert binary to decimal
decimal_number = convert_binary_to_decimal(random_binary)
print("Decimal Equivalent:", decimal_number)