import uuid
import hashlib


def hash_password(password):
    salt = uuid.uuid4().hex
    print('salt is: ' + salt + '\n')

    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password_matches(hashed_password, user_password):
    password, salt = hashed_password.split(':')

    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
