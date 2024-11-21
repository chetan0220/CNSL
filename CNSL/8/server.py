import socket
import cv2
import numpy as np
import os

# Function to encrypt/decrypt data using XOR with a given key
def xor_encrypt_decrypt(data, key):
    return bytes([b ^ key for b in data])

# Set up server
def start_server(host='localhost', port=8080, key=123):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening on port:", port)
    
    conn, addr = server_socket.accept()
    print("Connected by:", addr)

    # Receive encrypted data size
    data_size_str = conn.recv(1024).decode()
    if not data_size_str.isdigit():
        print("Error: Received invalid data size from client.")
        conn.close()
        server_socket.close()
        return
    
    data_size = int(data_size_str)
    conn.sendall(b"ACK")  # Acknowledge

    # Receive encrypted data
    encrypted_data = b""
    while len(encrypted_data) < data_size:
        packet = conn.recv(4096)
        if not packet:
            break
        encrypted_data += packet

    if len(encrypted_data) != data_size:
        print("Error: Received incomplete data from client.")
        conn.close()
        server_socket.close()
        return

    # Decrypt data
    decrypted_data = xor_encrypt_decrypt(encrypted_data, key)

    # Convert bytes to image
    np_data = np.frombuffer(decrypted_data, dtype=np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
    
    if img is None:
        print("Error: Failed to decode image data.")
        conn.close()
        server_socket.close()
        return

    # Check if the directory exists, if not, create it
    output_dir = "8"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the decrypted image in the 'decrypted_image' directory
    output_path = os.path.join(output_dir, "received_image.jpg")
    cv2.imwrite(output_path, img)
    print(f"Decrypted image saved as '{output_path}'")

    conn.close()
    server_socket.close()

# Start server
start_server()
