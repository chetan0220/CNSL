from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_rsa_keys():
    key = RSA.generate(2048)
    pvt_key = key.export_key()
    pub_key = key.publickey().export_key()
    return pvt_key, pub_key

def encrypt(message, receiver_pub_key):
    key = RSA.import_key(receiver_pub_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_msg = cipher.encrypt(message.encode())
    return encrypted_msg

def sign_msg(message, sender_pvt_key):
    key = RSA.import_key(sender_pvt_key)
    hash_obj = SHA256.new(message.encode())
    signer = pkcs1_15.new(key)
    signature = signer.sign(hash_obj)
    return signature

def decrypt(encrypted_msg, reveiver_pvt_key):
    key = RSA.import_key(reveiver_pvt_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_msg = cipher.decrypt(encrypted_msg).decode()
    return decrypted_msg

def verify_signature(msg, signature, x_pub):
    key = RSA.import_key(x_pub)
    hash_obj = SHA256.new(msg.encode())
    verifier = pkcs1_15.new(key)
    
    if verifier.verify(hash_obj, signature) is None:
        print("Signature is valid.")
    else:
        print("Signature is invalid.")


def hash_message(msg):
    hash_obj = SHA256.new(msg.encode())
    return hash_obj.hexdigest()
    

def main():
    # generate key prs for x and y
    x_pvt, x_pub = generate_rsa_keys()
    y_pvt, y_pub = generate_rsa_keys()
    print("Generated keys for X and Y")

    message = "HARRy potter 467uqeoh1##$&JFPE"

    # s1: encrypt message
    encrypted_msg = encrypt(message, y_pub)
    print("Message encrypted at X's end")

    # s2: digitally sign the message
    signature = sign_msg(message, x_pvt)
    print("Message signed at X's end")

    print("Message transmitted to Y")

    # s3: y decrypts the msg
    decrypted_msg = decrypt(encrypted_msg, y_pvt)
    print("Message decrypted at Y's end")
    print(f"Decrypted Message: {decrypted_msg}")

    # s4: verify signature
    verify_signature(decrypted_msg, signature, x_pub)

    # s5: check msg integrity
    hash = hash_message(decrypted_msg)
    print(f"Hash value of message: {hash}")

if __name__ == "__main__":
    main()