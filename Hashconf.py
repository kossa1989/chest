from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


"""
#Genrator random key
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

class InputPassword():

    def __init__(self,
                 input_password=input("Podaj hasło"),
                 input_password2=input("Podaj ponownie hasło do swojej bazy")
                 ):

        self.passwd = input_password
        self.passwd2 = input_password2

        #input_password = input('Podaj hasło do swojej bazy')
        #input_password2 = input('Podaj ponownie hasło do swojej bazy')

    def input_from_user(self):

        while self.passwd != self.passwd2:
            self.passwd = input('Podaj hasło do swojej bazy')
            self.passwd2 = input('Podaj ponownie hasło do swojej bazy')
        else:
            return self.passwd

    def key_from_pass(self):

            encode_password = self.passwd.encode()
            help_salt = b'{p\x91\x12\x04Q\x13\x0e"\x91n\xe8G\x99U\x9c\xb9\xd9\x94\xaf\xbc0\x17\xb3pd\x8a\x9bhn\x977'
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256,
                length=32,
                salt=help_salt,
                iterations=10000,
                backend=default_backend()
            )
            return base64.urlsafe_b64encode(kdf.derive(encode_password))


#key_from_pass()
#print(key_from_pass())
    def encrypt_str(self):
        mass = "to jest test"
        encoded = mass.encode() #zamienia na ciag byte

        k1 = self.key_from_pass()
        function_crypt = Fernet(k1)
        f_encode = function_crypt.encrypt(encoded)
        return f_encode


    def print_encode_str(self):
        print(InputPassword.encrypt_str(self))


    def decrypt_str(self):
        sth_str = InputPassword.encrypt_str(self)
        key = InputPassword.key_from_pass(self)
        function_decrypt = Fernet(key)
        decrypted = function_decrypt.decrypt(sth_str)
        mess_decrypted = decrypted.decode()
        return mess_decrypted
        print(mess_decrypted)

    def print_decrypt_str(self):
        print(InputPassword.decrypt_str(self))

x = InputPassword()
x.input_from_user()
x.key_from_pass()
x.encrypt_str()
x.print_encode_str()
x.decrypt_str()
x.print_decrypt_str()
