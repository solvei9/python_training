import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(random.choice(symbols) for i in range(random.randrange(maxlen)))


def random_phone():
    symbols = string.digits + " " + "-"
    return "+" + "".join(random.choice(symbols) for i in range(12))


def random_email():
    symbols = string.ascii_letters + string.digits
    return ("".join(random.choice(symbols) for i in range(2, 12)) + "@"
            + "".join(random.choice(symbols) for i in range(2, 5)) + "."
            + "".join(random.choice(symbols) for i in range(2, 5)))
