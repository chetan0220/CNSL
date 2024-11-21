import socket
import time

def generate_key_pairs():
    p, q = 3, 11
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 7
    d = pow(e, -1, phi_n)
    return ((e, n), (d, n))

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join(chr(pow(c, d, n) + ord('a')) for c in ciphertext)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print("Server is ready...")

    public_key, private_key = generate_key_pairs()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    conn, _ = server.accept()

    # Send public key
    conn.send(f"{public_key[0]},{public_key[1]}".encode())

    # Receive and decrypt ciphertext
    ciphertext = list(map(int, conn.recv(1024).decode().split(',')))
    print(f"Received Ciphertext: {ciphertext}")

    start_time = time.time()
    plaintext = decrypt(private_key, ciphertext)
    print(f"Decryption time: {time.time() - start_time:.6f}s")
    print(f"Decrypted message: {plaintext}")

    # Send decrypted message back
    conn.send(plaintext.encode())
    conn.close()

if __name__ == "__main__":
    main()
