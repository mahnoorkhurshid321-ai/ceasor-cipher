# Function to encrypt text using Caesar Cipher
def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            # Convert letter to ASCII, shift it, wrap around using modulo
            encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)

        # Check if character is lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)

        # If space or special character, keep it unchanged
        else:
            encrypted_text += char

    return encrypted_text


# Function to decrypt text using Caesar Cipher
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        if char.isupper():
            decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)

        elif char.islower():
            decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted_text += char

    return decrypted_text


# Main Program
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(message, shift)
    print("Encrypted Message:", encrypted)

    decrypted = caesar_decrypt(encrypted, shift)
    print("Decrypted Message:", decrypted)