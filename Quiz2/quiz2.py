# Umut Çakan S006742 Computer Science
import sys

# Key dictionary for cipher.
key = { 'a' : 'n' , 'b' : 'o' , 'c' : 'p' , 'd' : 'q' , 'e' : 'r' , 'f' : 's' ,
'g' : 't' , 'h' : 'u' , 'i' : 'v' , 'j' : 'w' , 'k' : 'x' , 'l' : 'y' ,
'm' : 'z' , 'n' : 'a' , 'o' : 'b' , 'p' : 'c' , 'q' : 'd' , 'r' : 'e' ,
's' : 'f' , 't' : 'g' , 'u' : 'h' , 'v' : 'i' , 'w' : 'j' , 'x' : 'k' ,
'y' : 'l' , 'z' : 'm' , 'A' : 'N' , 'B' : 'O' , 'C' : 'P' , 'D' : 'Q' ,
'E' : 'R' , 'F ' : 'S' , 'G' : 'T' , 'H' : 'U' , 'I' : 'V' , 'J' : 'W' ,
'K' : 'X' , 'L' : 'Y' , 'M' : 'Z' , 'N' : 'A' , 'O' : 'B' , 'P' : ' C' ,
'Q' : 'D' , 'R' : 'E' , 'S' : 'F' , 'T' : 'G' , 'U' : 'H' , 'V' : 'I' ,
'W' : 'J' , 'X' : 'K' , 'Y' : 'L' , 'Z' : 'M'
}

# The sentence is that is going to be encoded or decoded.
new_sentence = ""
# Exit variable.
is_exit = False

# Get processing type.
def get_processing_type():
    global is_exit
    # Take encode or decode type from the user.
    processing_type = input("Please enter 1 to encode, 2 to decode, 3 to exit: ")  
    # Check processing type.
    if processing_type == '1':
        # If processing type is 1, start encoding.
        encode_and_decode(user_input)
        # Print the result
        print("Encoded sentence is: ", new_sentence)  
        # Save the file.
        save_encoded_file(user_input)
    elif processing_type == '2':   
        # If processing type is 2, start decoding.
        encode_and_decode(user_input)
        # Print the result
        print("Decoded sentence is: ", new_sentence)  
        # Save the file.
        save_decoded_file(user_input)
    elif processing_type == '3':
        # Exit the program.
        is_exit = True
    else:
        print("Invalid processing type.")    
    
# Encode method.
def encode_and_decode(user_input):
    global new_sentence
    new_sentence = ""
    # Tokenize every word in input.
    for word in user_input.split():
        # Check letter by letter for each word.
        for letter in word:
            new_sentence += key[letter]  
        # Add whitespace after each word.    
        new_sentence += " " 
        
# Save encoded file to text file.        
def save_encoded_file(user_input):
    with open("secret.txt",'a',encoding = 'utf-8') as f: 
        # Print user input to first row.
        f.write("The input sentence: " + user_input + "\n")
        # Print encoded version to second row.
        f.write("The encoded sentence: " + new_sentence + "\n \n")

# Save decoded file to text file.        
def save_decoded_file(user_input):
    with open("secret.txt",'a',encoding = 'utf-8') as f: 
        # Print user input to first row.
        f.write("The input sentence: " + user_input + "\n")
        # Print decoded version to second row.
        f.write("The encoded sentence: " + new_sentence + "\n \n")         

# Take message from the user.
while not is_exit: 
    user_input = input("Please enter your message: ")
    # Check if there is any integer in string or not.
    if any(letter.isdigit() for letter in user_input):
        print("Invalid sentence, please do not use integer.")    
    else:
        get_processing_type()

    