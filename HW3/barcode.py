# Umut Çakan S006742 Computer Science

# Method that checks if barcode is valid or not.
def is_valid_barcode(barcode):
    # Check if input contains any letter.
    if not barcode.isnumeric():
        print_barcode_status(status_code = 1)
    # Check input length.
    elif not len(barcode) == 12 and not len(barcode) == 13:
        print_barcode_status(status_code = 2)
    # Check checksum of the barcode.    
    else:
        # Check for length of 12.
        if len(barcode) == 12:
            first_equation = int(barcode[1]) + int(barcode[3]) + int(barcode[5]) + int(barcode[7]) + int(barcode[9])
            second_equation = int(barcode[0]) + int(barcode[2]) + int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + int(barcode[10])
            last_digit_of_first_eq = first_equation % 10
            last_digit_of_second_eq = second_equation % 10
            multiplication_of_second = last_digit_of_second_eq * 3
            sum_of_first = last_digit_of_first_eq + (multiplication_of_second % 10)
            number_to_be_checked = 10 - (sum_of_first % 10)
            # Check if it is valid or not.
            if number_to_be_checked == int(barcode[11]):
                print_barcode_status(status_code = 4)
            else:
                print_barcode_status(status_code = 3)
        # Check for length of 13.        
        elif len(barcode) == 13:
            first_equation = int(barcode[1]) + int(barcode[3]) + int(barcode[5]) + int(barcode[7]) + int(barcode[9]) + int(barcode[11])
            second_equation = int(barcode[0]) + int(barcode[2]) + int(barcode[4]) + int(barcode[6]) + int(barcode[8]) + int(barcode[10])
            last_digit_of_first_eq = first_equation % 10
            last_digit_of_second_eq = second_equation % 10
            multiplication_of_second = last_digit_of_second_eq * 3
            sum_of_first = last_digit_of_first_eq + (multiplication_of_second % 10)
            number_to_be_checked = 10 - (sum_of_first % 10)
            # Check if it is valid or not.
            if number_to_be_checked == int(barcode[12]):
                print_barcode_status(status_code = 4)
            else:
                print_barcode_status(status_code = 3)
   
# Method that prints barcode status.    
def print_barcode_status(status_code):
    if status_code == 1:
        print("ERROR: Invalid barcode. There are letters in barcode.")
    elif status_code == 2:
        print("ERROR: Invalid barcode length. Barcode should be 12 or 13 digits.")
    elif status_code == 3:
        print("ERROR: Invalid barcode checksum.")
    elif status_code == 4:
        print("Valid barcode code.")
        