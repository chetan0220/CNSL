import socket
import cv2

# Function to encrypt/decrypt data using XOR with a given key
def xor_encrypt_decrypt(data, key):
    return bytes([b ^ key for b in data])

# Load image and convert to bytes
def load_image(image_path):
    img = cv2.imread(image_path)
    _, img_encoded = cv2.imencode('.jpg', img)
    return img_encoded.tobytes()

# Set up client
def start_client(host='localhost', port=8080, image_path='8/cat.jpg', key=123):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Load and encrypt image data
    image_data = load_image(image_path)
    encrypted_data = xor_encrypt_decrypt(image_data, key)

    # Send encrypted data size first
    client_socket.sendall(str(len(encrypted_data)).encode())
    client_socket.recv(1024)  # Wait for acknowledgment

    # Send encrypted image data
    client_socket.sendall(encrypted_data)

    client_socket.close()

# Start client with specified image path
start_client(image_path='8/cat.jpg')
