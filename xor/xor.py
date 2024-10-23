class XOR:
    """
    The class representation of the XOR "encryption system".
    """

    __is_single_block = False

    def __init__(self, key: str, single_block: bool = False):
        """ XOR class constructor """
        self.__is_single_block = single_block
        self.key = list(bytearray.fromhex(key))
        self.key.reverse()
        self.key_size = len(self.key)

    def encrypt(self, message: str) -> str:
        """ Encrypt a given message """
        # Transform the message into a list of bytes
        bytes = [ord(c) for c in message]
        xored = []

        if self.__is_single_block:
            assert len(bytes) == self.key_size, "In block mode, message and key must be the same size"
        # Add padding in stream mode
        elif len(bytes) % self.key_size != 0:
            bytes.extend([0 for _ in range(self.key_size - (len(bytes) % self.key_size))])
        # Apply XOR operation on each bytes of each block
        for block in [bytes[x:x+self.key_size] for x in range(0, len(bytes), self.key_size)]:
            xored.extend([block[i] ^ self.key[i] for i in range(self.key_size)])
        xored.reverse()
        return bytearray(xored).hex()

    def decrypt(self, message: str) -> str:
        """ Decrypt a given message """
        bytes = list(bytearray.fromhex(message))
        bytes.reverse()
        xored = []

        if self.__is_single_block:
            assert len(bytes) == self.key_size, "In block mode, message and key must be the same size"
        for block in [bytes[x:x+self.key_size] for x in range(0, len(bytes), self.key_size)]:
            xored.extend([block[i] ^ self.key[i] for i in range(self.key_size)])
        return bytearray(xored).decode().rstrip('\0')
