from cryptography.fernet import Fernet

# generate key and wrtie to file
def write_key():
    """ 
        Generates a key and saves to a file
    """
    key = Fernet.generate_key()
    with open("SYM.key", "wb") as key_file:
        key_file.write(key)
        
# load key
def load_key():
    """
        Loads the key from the current directory named `SYM.key`
    """
    return open ("SYM.key", "rb").read()

# call key
write_key()
key = load_key()

# create message for file
message = "Sammi's secret message for secure coding class!".encode()
print(f"ORIGINAL MESSAGE: \n " + str(message))

# initialize the Fernet class
f = Fernet(key)

# encrypt message
eMessage = f.encrypt(message)
# print fernet token
print("ENCRYPTED MESSAGE: \n " + str(eMessage))

# decrpyt message
dMessage = f.decrypt(eMessage)
print("DECRYPTED MESSAGE: \n " + str(dMessage))

