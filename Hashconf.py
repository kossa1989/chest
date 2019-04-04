from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


"""
def generate_random_key():
    file = open('key.key', 'wb')
    key = Fernet.generate_key()
    file.write(key)
    file.close()
    print (key)


def read_key():
    file = open('key.key', 'rb')
    key = file.read()
    print(key)


read_key()
"""
#Gen pass from input
def key_from_pass():
    input_password = 'x'
    input_password2 = 'y'
    while input_password != input_password2:
        input_password = input('Podaj hasło do swojej bazy')
        input_password2 = input('Podaj ponownie hasło do swojej bazy')
    else:
        encode_password = input_password.encode()
        help_salt = b'{p\x91\x12\x04Q\x13\x0e"\x91n\xe8G\x99U\x9c\xb9\xd9\x94\xaf\xbc0\x17\xb3pd\x8a\x9bhn\x977'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=help_salt,
            iterations=10000,
            backend=default_backend()
        )
        key_from_input_pass = base64.urlsafe_b64encode(kdf.derive(encode_password))
        return key_from_input_pass


#key_from_pass()
#print(key_from_pass())
def encrypt_str():
    mass = "to jest test"
    encoded = mass.encode() #zamienia na ciag byte

    k1 = key_from_pass()
    function_crypt = Fernet(k1)
    f_encode = function_crypt.encrypt(encoded)
    return f_encode

print(encrypt_str())


def decrypt_str():
    sth_str = encrypt_str()
    key = key_from_pass()
    function_decrypt = Fernet(key)
    decrypted = function_decrypt.decrypt(sth_str)
    mess_decrypted = decrypted.decode()
    return mess_decrypted

print(decrypt_str())