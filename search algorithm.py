#7 BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers
def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1  # Cannot find the number

    if numbers[index] == target:
        return index  # Can find the number

    return recursive_search(numbers, target, index + 1)  # Recursive call

# for example
numbers = [4, 2, 9, 7, 5, 1, 8, 3, 6]
target = int(input("Enter a number to search for: "))

# Perform the recursive search
result = recursive_search(numbers, target)

# Display the result
if result != -1:
    print("Number", target, "found at index", result)
else:
    print("Number", target, "not found in the list.")