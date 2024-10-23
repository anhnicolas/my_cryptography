from .tools import s_box, gmul

def sub_bytes(block: list[list]) -> None:
    """ 🔒 Subtitutes a block's bytes using a S-Box """
    for i in range(4):
        for j in range(4):
            block[i][j] = s_box[block[i][j]]

def shift_rows(b: list[list]) -> None:
    """ 🔒 Shift rows of a block """
    b[0][1], b[1][1], b[2][1], b[3][1] = b[1][1], b[2][1], b[3][1], b[0][1]
    b[0][2], b[1][2], b[2][2], b[3][2] = b[2][2], b[3][2], b[0][2], b[1][2]
    b[0][3], b[1][3], b[2][3], b[3][3] = b[3][3], b[0][3], b[1][3], b[2][3]

def __mix_column(column: list[int]) -> None:
    """ Mix a single column """
    a = [_ for _ in column]
    column[0] = gmul(2, a[0]) ^ gmul(3, a[1]) ^ gmul(1, a[2]) ^ gmul(1, a[3])
    column[1] = gmul(1, a[0]) ^ gmul(2, a[1]) ^ gmul(3, a[2]) ^ gmul(1, a[3])
    column[2] = gmul(1, a[0]) ^ gmul(1, a[1]) ^ gmul(2, a[2]) ^ gmul(3, a[3])
    column[3] = gmul(3, a[0]) ^ gmul(1, a[1]) ^ gmul(1, a[2]) ^ gmul(2, a[3])

def mix_columns(block: list[list[int]]) -> None:
    """ 🔒 Do magic shit to diffuse the block more """
    for i in range(4):
        __mix_column(block[i])
