# Design an experiment to estimate the amount of time to i) Generate key pair (RSA) ii) Encrypt n bit message (RSA) iii) Decrypt n bit message (RSA) As function of key size, experiment with different n-bit messages. Summarize your conclusions

import time

def generate_key_pairs():
    # s1: select p, q
    p = 3
    q = 11

    # s2: calculate n
    n = p*q

    # s3: calculate totient fn of n; since p,q are prime, phi_n = n-1
    phi_n = (p-1) * (q-1) 

    # s4: select e
    e = 7

    # s5: calculate d
    d = pow(e, -1, phi_n)

    return((e,n), (d,n))

def encrypt(public_key, plaintext):
    e, n = public_key
    message = [ord(char) - ord('a') for char in plaintext]
    ciphertext = [pow(char, e, n) for char in message]
    return ciphertext

def decrypt(private_key, cipher):
    d, n = private_key
    decrypted = [chr(pow(char, d, n) + ord('a')) for char in cipher]
    return ''.join(decrypted)

def main():
    start_time = time.time()
    public_key, private_key = generate_key_pairs()
    print(f"Key genrn time: {(time.time() - start_time):.6f}")
    print(f"Public: {public_key}, Pvt: {private_key}")
    
    plaintext = "dobby"

    start_time = time.time()
    encrypted_text = encrypt(public_key, plaintext)
    print(f"Encrypn time: {(time.time() - start_time):.6f}")
    print(f"Encrypted text: {encrypted_text}")

    start_time = time.time()
    decrypted_text = decrypt(private_key, encrypted_text)
    print(f"Decrypn time: {(time.time() - start_time):.6f}")
    print(f"Decrypted text: {decrypted_text}")
    
if __name__ == "__main__":
    main()