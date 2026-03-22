'''
Encrypt and decrypt all these files with AES in Counter Mode, using the code that you wrote previously. Employ
a key of 256 bits. Measure the time it takes to encrypt and decrypt each of the files. 
Make sure to produce statistically significant results (e.g. with standard deviation or confidence intervals).
Do results change if you run a fixed algorithm over the same file multiple times? 
And what if you run an algorithm over multiple randomly generated files of fixed size?
'''
# Step 1 - Implementation
import time
import os
from os import urandom 
import statistics
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = urandom(32)

def encrypt_file(input_file, output_file, key):
    nonce = urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    encryptor = cipher.encryptor()
    start = time.time()
    with open(input_file, "rb") as f:
        data = f.read()
    ct = encryptor.update(data) + encryptor.finalize()
    with open(output_file, "wb") as cphFile:
        cphFile.write(nonce)  # Save nonce for decryption
        cphFile.write(ct)
    end = time.time()
    total = end - start
    # print(f"Time for encrypting {input_file}: {total}")

def decrypt_file(input_file, output_file, key):
    start = time.time()
    with open(input_file, "rb") as f:
        nonce = f.read(16)
        ct = f.read()
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()
    data = decryptor.update(ct) + decryptor.finalize()
    with open(output_file, "wb") as decFile:
        decFile.write(data)
    end = time.time()
    total = end - start
    # print(f"Time for decrypting {input_file}: {total}")

folder_path = "random_files"
for file in os.listdir(folder_path):
    input_path = os.path.join(folder_path, file)
    encrypted_file = f"encrypted_{file}"
    decrypted_file = f"decrypted_{file}"
    encrypt_file(input_path, encrypted_file, key)
    decrypt_file(encrypted_file, decrypted_file, key)

# Step 2 - Statistical analysis
def measure_encrypt(input_file, key):
    times = []
    for i in range(50):
        start = time.time()
        encrypt_file(input_file, "temp.enc", key)
        end = time.time()
        times.append(end - start)
    return times

def measure_decrypt(encrypted_file, key):
    times = []
    for i in range(50):
        start = time.time()
        decrypt_file(encrypted_file, "temp.dec", key)
        end = time.time()
        times.append(end - start)
    return times
