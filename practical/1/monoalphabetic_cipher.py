# Implement monoalphabetic cipher

import random

def generate_key():
    aplhabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled = ''.join(random.sample(aplhabet, len(aplhabet)))
    key = dict(zip(aplhabet, shuffled))
    return key

def encrypt(plain_text, key):
    encrypted_txt = ''

    for char in plain_text:
        if char.isalpha():
            encrypted_txt += key[char.lower()].upper() if char.isupper() else key[char]
        else:
            encrypted_txt += char
    
    return encrypted_txt

def main():
    key = generate_key()
    print(key.items())
    plain_text = "i AM ai"
    encrypted_txt = encrypt(plain_text=plain_text, key=key)
    print(encrypted_txt)

if __name__ == '__main__':
    main()


'''
TC: O(n); n = len(plain_text); lookup --> O(1); generate_key() --> O(1)
Adv:
    - needs 26! tries to crack
Disadv:
    - vulnerable to freq analysis
    - once table is known cipher is completely broken
'''