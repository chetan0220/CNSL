# # pip install Pillow

from PIL import Image
import numpy as np

def xor_encrypt_decrypt(data, key):
    return bytearray([b ^ key for b in data])

image_path = "8/cat.jpg"
key = 5

with Image.open(image_path) as img:
    img = img.convert("RGB")
    pixel_data = np.array(img)

# Flatten the pixel data for encryption
flat_pixel_data = pixel_data.flatten()

# Encrypt the pixel data
encrypted_pixel_data = xor_encrypt_decrypt(flat_pixel_data, key)
encrypted_pixel_data = np.array(encrypted_pixel_data).reshape(pixel_data.shape)
print(encrypted_pixel_data)

# decrypt
decrypted_pixel_data = xor_encrypt_decrypt(encrypted_pixel_data.flatten(), key)
decrypted_pixel_data = np.array(decrypted_pixel_data).reshape(pixel_data.shape)
decrypted_img = Image.fromarray(decrypted_pixel_data, "RGB")

# Save and display the decrypted image
decrypted_image_path = "decrypted_image.png"
decrypted_img.save(decrypted_image_path)
print(f"Decrypted image saved as {decrypted_image_path}")

decrypted_img.show()