"""
  Midterm: Data Transmission App with Hashing and Encryption
  Samantha Harper
  09/18/2025
  This application will request user input, hash the input using SHA-256, 
  encrypt the input using AES, and decrypts the message and verifies its integrity. 
"""


#----------------------IMPORTS--------------------------------
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os


#--------------------USER INPUT------------------------------
message = input("Enter your message: ").encode() 


#-------------------HASH MESSAGE-----------------------------
hashed_message = hashlib.sha256(message).hexdigest()
print(f"Hashed Message: {hashed_message}")


#------------------AES ENCRYPTION----------------------------
# Generate 256-bit key
key = AESGCM.generate_key(bit_length=256)
# Generate Random 12-byte number to use once
num_used_once = os.urandom(12)
# Create Cipher
aesgcm = AESGCM(key)
#Encrypt the message
ciphtertext = aesgcm.encrypt(num_used_once, message, None)
print(f"Encrypted Message Hex: {ciphtertext.hex()}")


#-----------------AES DECRYPTION---------------------------------
# Decrypts ciphertext
decrypted_message = aesgcm.decrypt(num_used_once, ciphtertext, None)
print(f"Decrypted Message: {decrypted_message.decode()}")


#-----------------VERIFY HASH--------------------------------------
# Hash the decrypted message
decrypted_hash= hashlib.sha256(decrypted_message).hexdigest()
print(f"Decrypted Message Hash: {decrypted_hash}")
# Compare original and decripted hashes
if hashed_message == decrypted_hash:
    print("Integrity Check Passed!")
else:
    print("CAUTION: Integrity check FAILED!!")