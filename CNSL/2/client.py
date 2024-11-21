import socket
import time

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(c) - ord('a'), e, n) for c in plaintext]

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    # Receive public key
    e, n = map(int, client.recv(1024).decode().split(','))
    public_key = (e, n)
    print(f"Received Public Key: {public_key}")

    # Original plaintext message
    plaintext = "dobby"
    print(f"Original Message: {plaintext}")

    # Encrypt and send message
    start_time = time.time()
    ciphertext = encrypt(public_key, plaintext)
    print(f"Encryption time: {time.time() - start_time:.6f}s")
    print(f"Ciphertext: {ciphertext}")
    client.send(','.join(map(str, ciphertext)).encode())

    # Receive decrypted message
    decrypted_message = client.recv(1024).decode()
    print(f"Decrypted message from server: {decrypted_message}")
    client.close()

if __name__ == "__main__":
    main()
