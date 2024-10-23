from .tools import s_box

def sub_word(word: list):
    """ 🔑 Subtitutes a word's bytes using a S-Box """
    return [s_box[i] for i in word]

def rot_word(word: list):
    """ 🔑 Rotates a word front to rear (ABCD -> BCDA) """
    return word[1:] + word[:1]

def xor_words(a: list, b: list):
    """ 🔑 Applies XOR operator to each byte of a word """
    return [a[i]^b[i] for i in range(4)]

def add_round_key(block: list[list], key: list[list]):
    """ 🔑 Applies XOR operator to a block and a key """
    for i in range(4):
        for j in range(4):
            block[i][j] ^= key[i][j]
