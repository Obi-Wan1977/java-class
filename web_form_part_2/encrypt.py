def encrypt_with_shift(message, shift):
    """
    Encrypt or decrypt a message using Caesar cipher with the given shift.
    
    Args:
        message (str): The message to encrypt/decrypt
        shift (int): The shift value (positive for encryption, negative for decryption)
        
    Returns:
        str: The encrypted/decrypted message
    """
    result = ""
    
    for char in message:
        if char.isalpha():
            # Determine the case of the character
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            # Apply the shift and handle wrapping around the alphabet
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
            
    return result 