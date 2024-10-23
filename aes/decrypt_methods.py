from .tools import inv_s_box, gmul

def inv_sub_bytes(block: list[list[int]]) -> None:
    """ 🔓 Subtitutes a block's bytes using an inversed S-Box """
    for i in range(4):
        for j in range(4):
            block[i][j] = inv_s_box[block[i][j]]

def inv_shift_rows(b: list[list[int]]) -> None:
    """ 🔓 Reverse-shift rows of a block """
    b[0][1], b[1][1], b[2][1], b[3][1] = b[3][1], b[0][1], b[1][1], b[2][1]
    b[0][2], b[1][2], b[2][2], b[3][2] = b[2][2], b[3][2], b[0][2], b[1][2]
    b[0][3], b[1][3], b[2][3], b[3][3] = b[1][3], b[2][3], b[3][3], b[0][3]

def __inv_mix_column(column: list[int]) -> None:
    """ Mix a single column """
    a = [_ for _ in column]
    column[0] = gmul(14, a[0]) ^ gmul(11, a[1]) ^ gmul(13, a[2]) ^ gmul(9, a[3])
    column[1] = gmul(9, a[0]) ^ gmul(14, a[1]) ^ gmul(11, a[2]) ^ gmul(13, a[3])
    column[2] = gmul(13, a[0]) ^ gmul(9, a[1]) ^ gmul(14, a[2]) ^ gmul(11, a[3])
    column[3] = gmul(11, a[0]) ^ gmul(13, a[1]) ^ gmul(9, a[2]) ^ gmul(14, a[3])
    return column

def inv_mix_columns(block: list[list[int]]) -> None:
    """ 🔓 Do magic shit to un-diffuse the block """
    for i in range(4):
        __inv_mix_column(block[i])
