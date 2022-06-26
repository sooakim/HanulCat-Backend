from bcrypt import hashpw, gensalt, checkpw


def create_hash(password: str):
    password_bytes = password.encode(encoding='UTF-8')
    return bytes.decode(hashpw(password_bytes, salt=gensalt()), 'UTF-8')


def check_hash(hashedPassword: str, password: str):
    return checkpw(password.encode('UTF-8'), hashedPassword.encode('UTF-8'))