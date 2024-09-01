from cryptography.fernet import Fernet
import importlib.util

def encrypt_token(token):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_token = cipher.encrypt(token.encode())
    with open('token.dat', 'wb') as file:
        file.write(encrypted_token + b'\n' + key)
    print("token encrypted and saved in token.dat")

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("vault", "vault.py")
    vault = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vault)

    token = vault.TOKEN
    encrypt_token(token)