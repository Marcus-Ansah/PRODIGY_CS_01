def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the given text using the Caesar Cipher algorithm.

    Args:
    - text (str): The text to be encrypted or decrypted.
    - shift (int): The number of positions to shift the letters in the alphabet.
    - mode (str): 'encrypt' to encrypt the text, 'decrypt' to decrypt the text.
    """
    result = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return ''.join(result)


message = input("Enter the message to encrypt or decrypt: ")
shift = int(input("Enter the shift value (positive integer): "))
mode = input("Enter 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

if mode == 'encrypt':
    encrypted_message = caesar_cipher(message, shift, 'encrypt')
    print(f"Encrypted message: {encrypted_message}")
elif mode == 'decrypt':
    decrypted_message = caesar_cipher(message, shift, 'decrypt')
    print(f"Decrypted message: {decrypted_message}")
else:
    print("Invalid mode. Please enter either 'encrypt' or 'decrypt'.")