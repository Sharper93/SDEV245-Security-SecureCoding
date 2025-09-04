# RSA library - python implementation of RSA cryptographic algorithm
import rsa

# generate public and private key 
# suggested 1024 bytes as parm for message
publicKey, privateKey = rsa.newkeys(1024)

# string that needs to be encrypted
message = "Sammi's message for encryption and decryption using asymmetric keys"
print("ORIGINAL MESSAGE:\n" + message )

# rsa.encrypt method used to encrypt
eMessage = rsa.encrypt(message.encode(), publicKey)
print("ENCRYPTED MESSAGE:\n " + str(eMessage))

# DECRYPT
# rsa.decrypt method and private key
# returns encoded byte str, coverts to string with decode method
dMessage = rsa.decrypt(eMessage, privateKey).decode()
print("DECODED MESSAGE:\n " + dMessage)