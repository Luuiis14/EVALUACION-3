# negocio/encriptacion.py
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encriptar(texto):
    return cipher_suite.encrypt(texto.encode()).decode()

def desencriptar(encriptado):
    return cipher_suite.decrypt(encriptado.encode()).decode()
