from math import lcm, gcd
from .tools import int_to_lebytes, extended_euclidian, probably_prime

fermats = [
    65537, 257, 17, 5, 3
]

class RsaKey:
    """
    The class representation of a key (public or private)
    """

    mod : int = 0
    exponent : int = 0

    def __init__(self, exponent: int, mod: int) -> None:
        """ Rsa Key constructor """
        self.mod = mod
        self.exponent = exponent

    def __str__(self) -> str:
        """ Convert a key to a string """
        # Swap bytes to Little Endian
        exp_bytes = int_to_lebytes(self.exponent)
        mod_bytes = int_to_lebytes(self.mod)
        # Concat string
        return exp_bytes.hex() + "-" + mod_bytes.hex()

def key_from_hex(original: str) -> RsaKey:
    """ Parse a key from a string """
    split = original.split('-')
    assert len(split) == 2, "Key should be composed of two hex numbers"
    # Parse numbers from Little Endian
    exp_bytes = bytearray.fromhex(split[0])
    exp_bytes.reverse()
    mod_bytes = bytearray.fromhex(split[1])
    mod_bytes.reverse()
    return RsaKey(int(exp_bytes.hex(), 16), int(mod_bytes.hex(), 16))

class RsaPair:
    """
    The class representation of a Key-Pair
    """

    public: RsaKey = None
    private: RsaKey = None

    def __init__(self, p: int, q: int) -> None:
        """ 🔑 Generate a key pair """
        # Verify given numbers
        assert probably_prime(p), "P should be a prime number"
        assert probably_prime(q), "Q should be a prime number"
        # Init
        n = p * q
        d = 1
        e = 3
        # Compute λ(n)
        lambda_n = lcm(p - 1, q - 1)
        # Find e where 1 < e < λ(n)
        for f in fermats:
            if f < lambda_n and gcd(f, lambda_n):
                e = f
                break
        # Compute d where de ≡ 1 (mod λ(n))
        d = extended_euclidian(e, lambda_n)[1] % lambda_n
        self.public = RsaKey(e, n)
        self.private = RsaKey(d, n)

    def __str__(self) -> str:
        return f"public key: {str(self.public)}\nprivate key: {str(self.private)}"
