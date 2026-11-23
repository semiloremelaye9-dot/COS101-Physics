
# Function 1: Sum of numbers
def sum_numbers(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total


# Function 2: Average / Mean
def average(numbers):
    total = sum_numbers(numbers)
    return total / len(numbers)


# Function 3: Median and Mode
def median_mode(numbers):
    numbers.sort()

    # Find Median
    n = len(numbers)

    if n % 2 == 1:
        median = numbers[n // 2]
    else:
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    # Find Mode
    mode = numbers[0]
    highest_count = 0

    for num in numbers:
        count = numbers.count(num)

        if count > highest_count:
            highest_count = count
            mode = num

    return median, mode


# Main Program
my_numbers = [2, 4, 4, 6, 8]

print("Numbers:", my_numbers)
print("Sum:", sum_numbers(my_numbers))
print("Average:", average(my_numbers))

median, mode = median_mode(my_numbers)

print("Median:", median)
print("Mode:", mode)
