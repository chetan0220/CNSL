from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_rsa_keys():
    key = RSA.generate(2048)
    pvt_key = key.export_key()
    pub_key = key.publickey().export_key()
    return pvt_key, pub_key

def encrypt(message, pub_key):
    key = RSA.import_key(pub_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted

def sign(message, pvt_key):
    key = RSA.import_key(pvt_key)
    signer = pkcs1_15.new(key)
    hash_obj = SHA256.new(message.encode())
    sign = signer.sign(hash_obj)
    return sign

def decrypt(ciphertxt, pvt_key):
    key = RSA.import_key(pvt_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(ciphertxt).decode()
    return decrypted

def verify_signature(decrypted, signature, pub_key):
    key = RSA.import_key(pub_key)
    hash_obj = SHA256.new(decrypted.encode())
    verifier = pkcs1_15.new(key)
    if verifier.verify(hash_obj, signature) is None:
        print("Signature valid")
    else:
        print("invalid signature")
    
def hash_msg(msg):
    hash_obj = SHA256.new(msg.encode())
    return hash_obj.hexdigest()

def main():
    # s1: generate keys
    x_pvt, x_pub = generate_rsa_keys()
    y_pvt, y_pub = generate_rsa_keys()
    
    message = "hellow"

    # s2: encrypt the msg
    encrypted = encrypt(message, y_pub)
    print(encrypted)

    # s3: sign the msg
    signature = sign(message, x_pvt)

    # s4: decrypt
    decrypted = decrypt(encrypted, y_pvt)
    print(decrypted)

    # s5: verify signature
    verify_signature(decrypted, signature, x_pub)

    # s6: check integrity of msg
    dec_msg_hash = hash_msg(decrypted)
    msg_hash = hash_msg(message)
    print("integrity verified") if dec_msg_hash == msg_hash else print("msg tampered")

if __name__ == "__main__":
    main()

"""
PKCS - Public-Key Cryptography Standards
OAEP -  Optimal Asymmetric Encryption Padding
"""