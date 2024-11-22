from PIL import Image
import numpy as np

def xor_encrypt_decrypt(data, key):
    return bytearray([d ^ key for d in data])

image_path = "cat.jpg"
key = 5

with Image.open(image_path) as img:
    img = img.convert("RGB")
    pixel_data = np.array(img)

flat_pixel_data = pixel_data.flatten()

encrypted_data = xor_encrypt_decrypt(flat_pixel_data, key)
ecnrypted_data = np.array(encrypted_data).reshape(pixel_data.shape)
print(encrypted_data)

decrypted_data = xor_encrypt_decrypt(encrypted_data, key)
decrypted_data = np.array(decrypted_data).reshape(pixel_data.shape)    
decrypted_img = Image.fromarray(decrypted_data, "RGB")
decrypted_img.show()