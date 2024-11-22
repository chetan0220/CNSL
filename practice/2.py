def generate():
    p, q = 3, 11
    n = p * q
    phi_n = (p-1) * (q-1)
    e = 7
    d = pow(e, -1, phi_n)

    return((e,n), (d,n))

def encrypt(pub_key, plaintext):
    e, n = pub_key
    message = [ord(char) - ord('a') for char in plaintext]
    return [pow(char, e, n) for char in message]

def decrypt(pvt_key, cipher):
    d, n = pvt_key
    decrypted = [chr(pow(char, d, n) + ord('a')) for char in cipher]
    return "".join(decrypted)

def main():
    pub_key, pvt_key = generate()
    plaintext = "dobby"
    encrypted = encrypt(pub_key, plaintext)
    print(encrypted)
    decrypted = decrypt(pvt_key, encrypted)
    print(decrypted)

if __name__ == "__main__":
    main()
