# Umut Çakan S006742 Computer Science
# This program takes input(4 digit) seperated by commas and displays numbers that are divisible by 5.


while True:
    # Take string user input.
    input_numbers = input("Please enter 4 digit binary numbers: ")
    # Seperate all numbers by using comma splitter and add to the list.
    numbers = [x.strip() for x in input_numbers.split(',')]
    try:
        # Check if all the inputs are integer or not.
        [int(i) for i in numbers]
        # Check if all the inputs are 4 digit.
        if [len(i) != 4 for i in numbers].count(True) == 0:
            break
        else:
            # If not warn the user and take input again.
            print("All of your input is not 4 digit!")
            continue
    except ValueError:
        # If not warn the user and take input again.
        print("All of your input is not an integer!")
        continue
         
# Divisible number array.
divisibles = []

# Iterate all input numbers.
for number in numbers:
    # Convert them to decimal
    decimal_number = int(number, 2)
    # Check if it is divisible by 5 or not.
    if decimal_number % 5 == 0:
        # If it is divisible, add to the list.
        divisibles.append(number)

       
# Check if there is a divisible or not.
if len(divisibles) !=0:
    # If there is a number print result.
    print("The numbers that are divisible by 5 are: " + ",".join(divisibles))
else:
    # If there is not a number print this.
    print("None of the numbers are divisible by 5.")    
        
   