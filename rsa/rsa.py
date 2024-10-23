from .key import RsaKey, key_from_hex
from .tools import int_to_lebytes

class RSA:
    """
    The class representation of the RSA encryption system
    """

    __key: RsaKey = None

    def __init__(self, key: str, _: bool = False) -> None:
        self.__key = key_from_hex(key)

    def __concat_message(self, message: str) -> int:
        """ RSA Message concatenation """
        # Transform the string into a list of bytes
        bytes = bytearray([ord(c) for c in message])
        # Reverse endianness
        bytes.reverse()
        # Teansform to int
        return int(bytes.hex(), 16)

    def encrypt(self, message: str) -> str:
        """ RSA Encryption method """
        original = self.__concat_message(message)
        cipher = pow(original, self.__key.exponent, self.__key.mod)
        return int_to_lebytes(cipher).hex()

    def decrypt(self, message: str) -> str:
        """ RSA Decryption method """
        bytes = bytearray.fromhex(message)
        bytes.reverse()
        original = int(bytes.hex(), 16)
        decipher = pow(original, self.__key.exponent, self.__key.mod)
        bytes = bytearray.fromhex(f"{decipher:x}")
        bytes.reverse()
        return bytes.decode()

    def transform_key(self, key: str) -> str:
        """ RSA Key encryption / decryption for PGP """
        bytes = bytearray.fromhex(key)
        bytes.reverse()
        original = int(bytes.hex(), 16)
        decipher = pow(original, self.__key.exponent, self.__key.mod)
        return int_to_lebytes(decipher).hex()
