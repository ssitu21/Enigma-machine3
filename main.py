def format_text(text):
    return text.strip()


def create_cipher_dict(shift):
    """Create dictionaries for encryption and decryption"""
    encrypt_dict = {}
    decrypt_dict = {}
    
    # Lowercase letters (a-z)
    for i in range(26):
        original = chr(ord('a') + i)
        encrypted = chr(ord('a') + ((i + shift) % 26))
        encrypt_dict[original] = encrypted
        decrypt_dict[encrypted] = original
    
    # Uppercase letters (A-Z)
    for i in range(26):
        original = chr(ord('A') + i)
        encrypted = chr(ord('A') + ((i + shift) % 26))
        encrypt_dict[original] = encrypted
        decrypt_dict[encrypted] = original
    
    return encrypt_dict, decrypt_dict


def encrypt_with_dict(message, shift):
    """Encrypt a message using dictionary lookup"""
    encrypt_dict, _ = create_cipher_dict(shift)
    result = []
    
    for char in message:
        if char in encrypt_dict:
            result.append(encrypt_dict[char])
        else:
            result.append(char)
    
    return "".join(result)


def decrypt_with_dict(message, shift):
    """Decrypt a message using dictionary lookup"""
    _, decrypt_dict = create_cipher_dict(shift)
    result = []
    
    for char in message:
        if char in decrypt_dict:
            result.append(decrypt_dict[char])
        else:
            result.append(char)
    
    return "".join(result)


# MAIN PROGRAM

def main():
    print("===========================")
    print(" ENIGMA MACHINE SIMULATOR ")
    print("===========================")
    
    while True:
        print("\n-----------------------------")
        
        choice = input("Encrypt or decrypt? (e/d): ").lower()
        
        message = input("Enter your message: ")
        message = format_text(message)
        
        if not message:
            print("Error: Message cannot be empty")
            continue
        
        shift_input = input("Enter shift (1-25): ")
        
        if not shift_input.isdigit():
            print("Error: Shift must be a number")
            continue
        
        shift = int(shift_input)
        
        if shift < 1 or shift > 25:
            print("Error: Shift must be between 1 and 25")
            continue
        
        if choice == 'e':
            result = encrypt_with_dict(message, shift)
            
            print("\n=======================================")
            print("ENCRYPTION RESULT")
            print("=======================================")
            print("Original:  " + message)
            print("Encrypted: " + result)
            print("=======================================")
         
        elif choice == 'd': 
            result = decrypt_with_dict(message, shift)
            
            print("\n=======================================")
            print("DECRYPTION RESULT")
            print("=======================================")
            print("Original:  " + message)
            print("Decrypted: " + result)
            print("=======================================")
        else:
            print("Invalid choice")
            continue
        
        again = input("\nRun again? (yes/no): ").lower()
        if again != 'yes' and again != 'y':
            print("\nGoodbye")
            break


# Run the program
if __name__ == "__main__":
    main()