# Design and Implement your own encryption/ decryption algorithm using any programming language

'''
Start with a fixed shift and increase it as we move forward in the word

Example: 

Plaintext: HELLO

First letter shifted by 3
Second letter shifted by 4
Third letter shifted by 5
Fourth letter shifted by 6
Fifth letter shifted by 7

Encrypted: KIQRV

'''
def encrypt(text, start_shift):
    result = []
    shift = start_shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
            shift += 1
        else:
            result.append(char)
    
    return ''.join(result)

def decrypt(text, start_shift):
    result = []
    shift = start_shift
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base - shift) % 26 + base)
            result.append(new_char)
            shift += 1
        else:
            result.append(char)
    
    return ''.join(result)

plaintext = "HELLO"
start_shift = 3

encrypted_text = encrypt(plaintext, start_shift)
print(f"Encrypted: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, start_shift)
print(f"Decrypted: {decrypted_text}")