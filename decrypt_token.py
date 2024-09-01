from cryptography.fernet import Fernet

def decrypt_token():
    with open('token.dat', 'rb') as file:
        data = file.read()
    encrypted_token, key = data.rsplit(b'\n', 1)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_token).decode()

if __name__ == "__main__":
    decrypt_token()
