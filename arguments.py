from sys import argv
from enum import Enum

class CryptSystem(str, Enum):
    """ Enum type that represents encrpytion systems """
    XOR = "xor"
    AES = "aes"
    RSA = "rsa"
    PGP_XOR = "pgp-xor"
    PGP_AES = "pgp-aes"

class WorkMode(str, Enum):
    """ Enum type that reprensents working modes """
    ENCRYPT = "-c"
    DECRYPT = "-d"
    GENERATE = "-g"

class InputMode(Enum):
    STREAM = 0
    BLOCK = 1

class Arguments:
    """
    Parses the arguments into a usable form
    """

    system: CryptSystem = None
    work_mode: WorkMode = None
    input_mode: InputMode = None
    key: str = ""
    primes: (int) = ()

    def __argc_should_be(self, query: int):
        """ Checks if there is just enough arguments """
        if len(argv) != query:
            raise ValueError("Bad arguments count, expected " + str(query))

    def __init__(self) -> None:
        """ Constructor for argument parsing """
        # Handle help option
        if len(argv) == 2 and argv[1] == "-h":
            self.print_usage()
            exit(0)
        # Need at least 3 arguments (+1 for command) in any case
        if len(argv) < 4:
            raise ValueError("Not enough arguments")
        # Parse arguments using Enums, will throw if incorrect
        self.system = CryptSystem(argv[1])
        self.work_mode = WorkMode(argv[2])

        # Disallow use of "-g" if not using RSA
        if self.work_mode == WorkMode.GENERATE and self.system != CryptSystem.RSA:
            raise ValueError("Bad arguments combo:", self.system.value, self.work_mode.value)

        if self.work_mode == WorkMode.GENERATE:
            # Expect 4 (+1) arguments and set primes
            self.__argc_should_be(5)
            p = bytearray.fromhex(argv[3])
            p.reverse()
            q = bytearray.fromhex(argv[4])
            q.reverse()
            self.primes = (int(p.hex(), 16), int(q.hex(), 16))
        elif argv[3] == '-b':
            # Expect 4 (+1) arguments and set key & block mode
            self.__argc_should_be(5)
            self.input_mode = InputMode.BLOCK
            self.key = argv[4]
        else:
            # Expect 3 (+1) arguments and set key
            self.__argc_should_be(4)
            self.key = argv[3]

    @staticmethod
    def print_usage():
        print("USAGE")
        print("./my_pgp CRYPTO_SYSTEM MODE [OPTIONS] [key]\n")
        print("DESCRIPTION")
        print("The MESSAGE is read from standard input\n")
        print("CRYPTO_SYSTEM")
        print("\txor\tcomputation using XOR algorithm")
        print("\taes\tcomputation using 128-bit AES algorithm")
        print("\trsa\tcomputation using RSA algorithm")
        print("\tpgp-xor\tcomputation using both RSA and XOR algorithm")
        print("\tpgp-aes\tcomputation using both RSA and 128-bit AES algorithm\n")
        print("MODE")
        print("\t-c\tMESSAGE is clear and we want to cipher it")
        print("\t-d\tMESSAGE is ciphered and we want to decipher it")
        print("\t-g\tP Q for RSA only: Don't read a MESSAGE, but instead generate a public and")
        print("\t\tprivate key pair from the prime number P and Q\n")
        print("OPTIONS")
        print("\t-b\tfor XOR, AES and PGP, only works on one block. The MESSAGE and the")
        print("\t\tsymmetric key must be the same size")
        print("key\tKey used to cipher/decipher MESSAGE (incompatible with -g MODE)")