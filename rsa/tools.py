from math import log2
from random import randrange

def probably_prime(n: int, k: int = 40) -> bool:
    """ Check if a number is probably prime by using Miller Rabin algorithm """
    # Basic tests
    if n < 2 or n % 2 == 0:
        return False
    # Miller Rabin from Wikipedia's pseudo code
    d, s, y = n - 1, 0, 0
    # Compute D and S
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        a = randrange(2, n - 2)
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True

def extended_euclidian(a: int, b: int) -> (int):
    """ 🔧 Euclid's extended algorithm """
    # Recursive implementation from Wikipedia
    if b == 0:
        return a, 1, b
    x, y, z = extended_euclidian(b, a % b)
    return x, z, y - (a // b) * z

def int_to_lebytes(n: int) -> bytearray:
    """ 🔧 Gives a Little Endian bytearray of a number """
    bytes = bytearray()
    while n > 0:
        bytes.append(n % 256)
        n //= 256
    return bytes
