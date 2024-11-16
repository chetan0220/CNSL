# Demonstrate how Diffie-Hellman key exchange works with Man-In-The-Middle attack.

import random

def diffie_hellman_key_exchange(prime, alpha, private_key):
    return pow(alpha, private_key, prime)

def mitm(prime, alpha, alice_private, bob_private):
    # s1: alice sends her public key to darth
    alice_public = diffie_hellman_key_exchange(prime, alpha, alice_private)

    #s2: darth intercepts alice's public key and sends his own public key to bob
    darth_private = random.randint(1, prime-1)
    darth_public = diffie_hellman_key_exchange(prime, alpha, darth_private)

    # bob receives darth's public key instead of alics's
    
    # s3 bob sends his public key and darth intercepts it instead of alice
    bob_public = diffie_hellman_key_exchange(prime, alpha, bob_private)

    # s4 darth calculates secret key
    secret_key_with_alice = diffie_hellman_key_exchange(prime, darth_public, alice_private)
    secret_key_with_bob = diffie_hellman_key_exchange(prime, darth_public, bob_private)

    print(f"Alice public key: {alice_public}")
    print(f"Bob public key: {bob_public}")
    print(f"Darth public key: {darth_public}")
    print(f"Secret key shared with Alice: {secret_key_with_alice}")
    print(f"Secret key shared with Bob: {secret_key_with_bob}")

def main():
    prime = 23
    alpha = 5
    alice_private = random.randint(1, prime-1)
    bob_private = random.randint(1, prime-1)
    mitm(prime, alpha, alice_private, bob_private)

if __name__ == "__main__":
    main()

'''
Alice  --->  Darth  --->  Bob
secret key is different hence proved mitm attack has occcured
'''
