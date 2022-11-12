import string
import random


def get_random_password(n: int) -> str:
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = random.sample(chars, n)
    password = "".join(password)
    return password
    # TODO написать функцию генерации случайных паролей


print(get_random_password(8))
