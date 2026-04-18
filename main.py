# ============================================
# ENIGMA MACHINE PROJECT (CAESAR CIPHER)
# PSEUDOCODE:
# 1. Create format_text() to remove whitespace using .strip()
# 2. Create create_cipher_dict(shift):
#    - Loop i from 0 to 25 for lowercase letters
#    - Map original to encrypted using (i + shift) % 26
#    - Map encrypted back to original for decrypt
#    - Repeat for uppercase letters
#    - Return both dictionaries
# 3. Create encrypt_with_dict(message, shift):
#    - Call create_cipher_dict to get encrypt_dict
#    - Loop through each character in message
#    - If char is in dict, replace with encrypted version
#    - If not (spaces/punctuation), keep unchanged
#    - Join and return result
# 4. Create decrypt_with_dict(message, shift):
#    - Same as encrypt but using decrypt_dict
# 5. Main program:
#    - Print welcome message
#    -
#  Loop until user quits
#    - Ask for encrypt/decrypt choice (e/d)
#    - Get message and strip whitespace
#    - Get shift number (1-25 only)
#    - Validate shift is digit and between 1-25
#    - Call appropriate function based on choice
#    - Print formatted result
#    - Ask user if they want to run again
# ============================================


def format_text(text):
    return text.strip()

# Function to encrypt message
def encrypt(message_list, shift):
    result = []

    # Loop through each character
    for char in message_list:

        # Check if character is a letter
        if char.isalpha():

            # Shift character forward
            new_char = chr(ord(char) + shift)

            # Wrap around alphabet
            if char.islower() and new_char > "z":
                new_char = chr(ord(new_char) - 26)
            elif char.isupper() and new_char > "Z":
                new_char = chr(ord(new_char) - 26)

            result.append(new_char)

        else:
            result.append(char)

    return "".join(result)

# Function to decrypt message
def decrypt(message_list, shift):
    result = []

    # Loop through each character
    for char in message_list:

        # Check if character is a letter
        if char.isalpha():

            # Shift character backward
            new_char = chr(ord(char) - shift)

            # Wrap around alphabet
            if char.islower() and new_char < "a":
                new_char = chr(ord(new_char) + 26)
            elif char.isupper() and new_char < "A":
                new_char = chr(ord(new_char) + 26)

            result.append(new_char)

        else:
            result.append(char)

    return "".join(result)

# Main program
def main():
    print("===========================")
    print(" ENIGMA MACHINE SIMULATOR ")
    print("===========================")


# Run the program
if __name__ == "__main__":
    main()