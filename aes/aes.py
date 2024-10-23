from .tools import r_con, bytes_to_words, get_block, string_to_words, words_to_hexstring, hexstring_to_words, words_to_string, reverse_bytes_composite
from .encrypt_methods import sub_bytes, shift_rows, mix_columns
from .decrypt_methods import inv_sub_bytes, inv_shift_rows, inv_mix_columns
from .key_methods import add_round_key, rot_word, sub_word, xor_words

class AES:
    """
    The class representation of the AES-128 bit encryption system.
    Used for both encryption and decryption.
    """

    __is_single_block = False
    __expanded_key : list[list[int]] = []

    def __key_enxpansion(self, key: list[list[int]]):
        """ Expands the given key to the 11 block long master key """
        # Copy the first 4 words from original key
        for i in range(4):
            self.__expanded_key.append(key[i])

        # Generate the remaining words
        for i in range(4, 44):
            word = self.__expanded_key[i - 1]
            if i % 4 == 0:
                # Every new word
                word = rot_word(word)
                word = sub_word(word)
                word = xor_words(word, r_con[i // 4])
            word = xor_words(self.__expanded_key[i - 4], word)
            self.__expanded_key.append(word)

    def __init__(self, key: str, single_block: bool = False):
        """ AES Constructor """
        self.__is_single_block = single_block
        bytes = reverse_bytes_composite(bytearray.fromhex(key))
        # Secret key length must be 16 bytes in block mode
        assert len(bytes) == 16
        master_key = bytes_to_words(bytes)
        self.__key_enxpansion(master_key)

    def __encrypt_block(self, block: list[list[int]]) -> list[list[int]]:
        """ Encrypts a single block of data """
        # Start
        key = get_block(self.__expanded_key, 0)
        add_round_key(block, key)
        # 9 Standard rounds
        for i in range(1, 10):
            key = get_block(self.__expanded_key, i)
            sub_bytes(block)
            shift_rows(block)
            mix_columns(block)
            add_round_key(block, key)
        # Final round (no mixing)
        key = get_block(self.__expanded_key, 10)
        sub_bytes(block)
        shift_rows(block)
        add_round_key(block, key)

    def encrypt(self, message: str) -> str:
        """ AES Encryption Method """
        if self.__is_single_block:
            assert len(message) == 16, "In block mode, Input must be 16 bytes long"
        words = string_to_words(message)
        # Encrypt block per block
        for i in range(len(words) // 4):
            block = get_block(words, i)
            self.__encrypt_block(block)
        for w in words:
            w.reverse()
        return words_to_hexstring(words)

    def __decrypt_block(self, block: list[list[int]]) -> list[list[int]]:
        """ Decrypts a single block of data """
        # Inverted final round
        key = get_block(self.__expanded_key, 10)
        add_round_key(block, key)
        inv_shift_rows(block)
        inv_sub_bytes(block)
        # 9 Inverted rounds
        for i in range(9, 0, -1):
            key = get_block(self.__expanded_key, i)
            add_round_key(block, key)
            inv_mix_columns(block)
            inv_shift_rows(block)
            inv_sub_bytes(block)
        # Inverted Start (End)
        key = get_block(self.__expanded_key, 0)
        add_round_key(block, key)

    def decrypt(self, cipher: str) -> str:
        """ AES Decryption Method """
        if self.__is_single_block:
            assert len(bytearray.fromhex(cipher)) == 16, "In block mode, Input must be 16 bytes long"
        words = hexstring_to_words(cipher)
        for w in words:
            w.reverse()
        # Decrypt block per block
        for i in range(len(words) // 4):
            block = get_block(words, i)
            self.__decrypt_block(block)
        return words_to_string(words)
