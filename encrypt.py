from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hashed(password):
    return context.hash(password)
