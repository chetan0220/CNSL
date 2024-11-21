# Implement monoalphabetic cipher

import random
def generate_key():
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    shuffled = ''.join(random.sample(alphabets, len(alphabets)))
    return dict(zip(alphabets, shuffled))

def reverse_key(key):
    return {v: k for k,v in key.items()}

def encrypt(plaintext, key):
    encrypted = ''
    for char in plaintext:
        if char.isalpha():
            encrypted += key[char.lower()].upper() if char.isupper() else key[char]
        else:
            encrypted += char
    return encrypted

def decrypt(plaintext, reversed_key):
    decrypted = ''
    for char in plaintext:
        if char.isalpha():
            decrypted += reversed_key[char.lower()].upper() if char.isupper() else reversed_key[char]
        else:
            decrypted += char
    return decrypted

def main():
    key = generate_key()
    print(key)
    plaintext = "i am AI 8"
    cipher = encrypt(plaintext, key)
    print(cipher)

    reversed_key = reverse_key(key)
    print(reversed_key)
    decrypted = decrypt(cipher, reversed_key)
    print(decrypted)

if __name__ == "__main__":
    main()

'''
TC: O(n); n = len(plain_text); lookup --> O(1); generate_key() --> O(1)
Adv:
    - needs 26! tries to crack
Disadv:
    - vulnerable to freq analysis
    - once table is known cipher is completely broken
'''
