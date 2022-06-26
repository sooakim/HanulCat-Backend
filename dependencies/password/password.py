from bcrypt import hashpw, gensalt


def create_hash(password: str):
    password_bytes = password.encode(encoding='UTF-8')
    return hashpw(password_bytes, salt=gensalt())