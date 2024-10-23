from xor import XOR
from aes import AES
from rsa import RSA, RsaPair
from arguments import Arguments, CryptSystem, WorkMode, InputMode

def get_input(mode: InputMode) -> str:
    lines: list[str] = []
    try:
        while True:
            lines.append(input())
            if mode == InputMode.BLOCK:
                break
    except:
        pass # Pass keyboard interrupts
    return "\n".join(lines)

def main():
    args = Arguments()

    if args.work_mode == WorkMode.GENERATE:
        keys = RsaPair(args.primes[0], args.primes[1])
        print(keys)
        return

    # Get user input
    user_input: str = get_input(args.input_mode)
    is_single_block: bool = args.input_mode == InputMode.BLOCK

    systems = {
        CryptSystem.XOR: XOR,
        CryptSystem.AES: AES,
        CryptSystem.RSA: RSA,
    }

    if args.system in systems:
        system = systems[args.system](args.key, is_single_block)
        result = system.encrypt(user_input) if args.work_mode == WorkMode.ENCRYPT else system.decrypt(user_input)
        print(result)

    if args.system in (CryptSystem.PGP_XOR, CryptSystem.PGP_AES):
        keys = args.key.split(':')
        assert len(keys) == 2, "2 keys must be provided to use PGP"
        rsa_key = RSA(keys[1]).transform_key(keys[0])
        use_key = keys[0] if args.work_mode == WorkMode.ENCRYPT else rsa_key
        system = XOR(use_key) if args.system == CryptSystem.PGP_XOR else AES(use_key)
        if args.work_mode == WorkMode.ENCRYPT:
            print(rsa_key)
            print(system.encrypt(user_input))
        else:
            print(system.decrypt(user_input))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit(84)
