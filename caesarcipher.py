def encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character based on the given shift value
            shifted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)

def main():
    # Get user input
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the message
    encrypted_message = encrypt(message, shift)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, shift)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()