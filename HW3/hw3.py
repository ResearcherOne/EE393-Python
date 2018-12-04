# Umut Çakan S006742 Computer Science
# This program takes barcode input from the user and checks if it is valid or not.
import barcode

# Get the input from the user.
try:
    barcode_input = input("Please enter the barcode: ")
    if not barcode_input:
        raise ValueError("ERROR: Empty input. Please enter the barcode.")
except ValueError as e:
    print(e)
   
# Check if the barcode is valid or not.    
barcode.is_valid_barcode(barcode_input)    