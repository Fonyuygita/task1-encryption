from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import unpad


def decrypt_file(input_file, output_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
        
    plaintext = cipher.decrypt(ciphertext)
    
    # Remove the padding from the plaintext
    plaintext = unpad(plaintext, AES.block_size)
    
    with open(output_file, 'wb') as f:
        f.write(plaintext)

# Decrypt the encrypted PDF file
key=b'mysecretpassword'
decrypt_file("encrypted.txt", "decrypted.txt", key)
