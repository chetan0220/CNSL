import random

def key_exchange(alpha, alice_pvt, prime):
    return pow(alpha, alice_pvt, prime)

def mitm(prime, alpha, alice_pvt, bob_pvt):
    #s1 : alice sends pub key to bob but goes to darth
    alice_pub = key_exchange(alpha, alice_pvt, prime)

    # s2: darth receives alices pub key and sends his own pub key to bob instead of alice's
    darth_pvt = random.randint(1, prime-1)
    darth_pub = key_exchange(alpha, darth_pvt, prime)

    # s3: bob sends his pub key to alice but goes to darth
    bob_pub = key_exchange(alpha, bob_pvt, prime)

    # s4: darth calculates secret keys for further comms
    alice_secret = key_exchange(darth_pub, alice_pvt, prime)
    bob_secret = key_exchange(darth_pub, bob_pvt, prime)

    print(f"Alice public key: {alice_pub}")
    print(f"Bob public key: {bob_pub}")
    print(f"Darth public key: {darth_pub}")
    print(f"Secret key shared with Alice: {alice_secret}")
    print(f"Secret key shared with Bob: {bob_secret}")


def main():
    prime = 23
    alpha = 5
    alice_pvt = random.randint(1, prime-1) 
    bob_pvt = random.randint(1, prime-1)
    mitm(prime, alpha, alice_pvt, bob_pvt)

if __name__ == "__main__":
    main()