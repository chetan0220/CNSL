# A message is to be transmitted using network resources from one machine to another calculate and demonstrate the use of a Hash value equivalent to SHA-1.

import struct

# Constants for SHA-1
H0, H1, H2, H3, H4 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0

def left_rotate(n, b):
    """Left rotate a 32-bit integer n by b bits."""
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF

def sha1(message):
    """Compute the SHA-1 hash of a message."""
    # Pre-processing
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8

    # Append the bit '1' to the message
    message += b'\x80'

    # Append 0 <= k < 512 bits '0', so that the resulting message length (in bits) is congruent to 448 (mod 512)
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    # Append length of message (before pre-processing), in bits, as 64-bit big-endian integer
    message += struct.pack('>Q', original_bit_len)

    # Process the message in successive 512-bit chunks
    hash_pieces = [H0, H1, H2, H3, H4]

    # Process each 512-bit chunk
    for i in range(0, len(message), 64):
        chunk = message[i:i+64]
        w = [0] * 80

        # Break chunk into sixteen 32-bit big-endian words w[i], 0 <= i <= 15
        for j in range(16):
            w[j] = struct.unpack('>I', chunk[j*4:j*4+4])[0]

        # Extend the sixteen 32-bit words into eighty 32-bit words
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)

        # Initialize hash value for this chunk
        a, b, c, d, e = hash_pieces

        # Main loop
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Add this chunk's hash to result so far
        hash_pieces = [
            (hash_pieces[0] + a) & 0xFFFFFFFF,
            (hash_pieces[1] + b) & 0xFFFFFFFF,
            (hash_pieces[2] + c) & 0xFFFFFFFF,
            (hash_pieces[3] + d) & 0xFFFFFFFF,
            (hash_pieces[4] + e) & 0xFFFFFFFF,
        ]

    # Produce the final hash value (big-endian) as a hex string
    return ''.join(f'{piece:08x}' for piece in hash_pieces)

# Example usage
message = input("Enter the message: ")
hash_value = sha1(message.encode())
print("SHA-1 hash:", hash_value)
