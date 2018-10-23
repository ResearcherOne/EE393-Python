# Umut Cakan Computer Science S006742

# Fibonacci list. First and second terms are static.
fib_list = [0, 1]
# Current index.
CURRENT_INDEX = 2

# Function for the checking input is a Fibonacci number or not.
def check_fibonacci_number():
    global CURRENT_INDEX
    # Get the fibonacci numbers that are less or equal to input value.
    # Because we will not need to check fib numbers that are higher than our input.
    while fib_list[CURRENT_INDEX - 1] < NUMBER_TO_BE_CHECKED:
        fib_list.append(fib_list[CURRENT_INDEX - 1] + fib_list[CURRENT_INDEX - 2])
        CURRENT_INDEX += 1
    # Check if the input value is in that list or not.
    if NUMBER_TO_BE_CHECKED not in fib_list:
        print("Your number is not a Fibonacci number.")
    else:
        print("Your number is a Fibonacci number.")


# Get number to be checked from user.
while True:
    try:
        NUMBER_TO_BE_CHECKED = int(input("Please enter the number to check: "))
    # If it is not an integer throw an error and wait for another input.
    except ValueError:
        print("Your input is not an integer!")
        continue
    # If it is an integer, proceed.    
    else:
        check_fibonacci_number()
        break
