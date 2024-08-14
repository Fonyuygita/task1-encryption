from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()
        
    # Pad the plaintext to be a multiple of 16 bytes
    plaintext = pad(plaintext, AES.block_size)
    
    ciphertext = cipher.encrypt(plaintext)
    
    with open(output_file, 'wb') as f:
        f.write(ciphertext)
 
 # Generate a random 16-byte key
key = b'mysecretpassword'

# Encrypt a PDF file
encrypt_file("input.txt", "encrypted.txt", key)