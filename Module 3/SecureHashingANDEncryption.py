"""
Secure Hashing and Encryption Assignment
Samantha Harper
09/10/2025
This Python Application provides a simple command-line interface for performing secure hashing. 
Caesar cipher encryption/decryption and digital signature operations using open SSL. 
It also includes RBAC for user authentication. 
"""

import hashlib
import os
import shutil
import subprocess
import sys
from getpass import getpass
from pathlib import Path
from typing import Tuple

#--------------------SHA-256 HASHING------------------------------
def sha256_str(s: str) -> str: 
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


#-----------------USER AUTHENTICATION------------------------------
USERS = {
    # username: (sha256(password), role)
    "admin": (sha256_str("admin123"), "admin"),
    "alice": (sha256_str("userpass"), "user"),
}

#Authentication / RBAC
def login() -> Tuple[str, str]:
    print("=== Login ===")
    username = input("Username: ").strip()
    password = getpass("Password: ")
    rec = USERS.get(username)
    if not rec or sha256_str(password) != rec[0]:
        print("Invalid credentials.\n")
        sys.exit(1)
    role = rec[1]
    print(f"Welcome, {username}! Role: {role}\n")
    return username, role

def require_role(required:str, actual: str):
    if actual != required:
        raise PermissionError(f"This action requires role '{required}'. Your Role is '{actual}'")


#--------------------------CAESAR CIPHER---------------------------------
def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    if decrypt:
        shift = -shift
    result = ""
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else: 
            result += char
    return result


#========================DIGITAL SIGNATURE (OPENSSL)-------------------------------
def generate_keys():
    subprocess.run(["openssl", "genpkey", "-algorithm", "RSA", "-out", "private_key.pem"])
    subprocess.run(["openssl", "rsa", "-pubout", "-in", "private_key.pem", "-out", "public_key.pem"])
    
def sign_file(file_path: str):
    subprocess.run(["openssl", "dgst", "-sha256", "-sign", "private_key.pem", "-out", "signature.bin", file_path])

def verify_signature(file_path: str):
    subprocess.run(["openssl", "dgst", "-sha256", "-verify", "public_key.pem", "-signature", "signature.bin", file_path])
    
    
# ---------------- Main Menu ----------------
def main():
    username, role = login()

    while True:
        print("Choose an option:")
        print("1. Hash a string")
        print("2. Encrypt text (Caesar cipher)")
        print("3. Decrypt text (Caesar cipher)")
        print("4. Generate RSA keys (admin only)")
        print("5. Sign a file")
        print("6. Verify a signature")
        print("00. Exit")

        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                s = input("Enter string: ")
                print("SHA-256:", sha256_str(s))
            elif choice == "2":
                text = input("Text to encrypt: ")
                shift = int(input("Shift value: "))
                print("Encrypted:", caesar_cipher(text, shift))
            elif choice == "3":
                text = input("Text to decrypt: ")
                shift = int(input("Shift value: "))
                print("Decrypted:", caesar_cipher(text, shift, decrypt=True))
            elif choice == "4":
                require_role("admin", role)
                generate_keys()
                print("Keys generated.")
            elif choice == "5":
                path = input("File to sign: ")
                sign_file(path)
                print("File signed.")
            elif choice == "6":
                path = input("File to verify: ")
                verify_signature(path)
            elif choice == "00":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()