import uuid
import hashlib


class PasswordEncryptor:

    @staticmethod
    def hash_password(password):
        salt = uuid.uuid4().hex
        print('salt is: ' + salt)

        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    @staticmethod
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')

        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
