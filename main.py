import argparse


def hexdump(in_path: str, /, line_count=20, offset=0):
    with open(in_path, "rb") as in_stream:
        __hexdump(in_stream, line_count, offset)


def __hexdump(inp, line_count, offset):
    inp.read(offset)

    adr = offset
    line_acc = 0
    while (bs := inp.read(16)) \
            and (True if line_count is None else line_acc < line_count):
        __print_line(adr, bs)

        adr += len(bs)
        line_acc += 1


def __print_line(adr, bs):
    print(f"{adr:8X}   ", end="")

    for b in bs:
        print(f"{b:02X} ", end="")

    for i in range(len(bs), 16):
        print("   ", end="")
    print("   ", end="")

    for b in bs:
        print(__convert_char(b), end="")

    for i in range(len(bs), 16):
        print(" ", end="")
    print()


def __convert_char(c):
    if c <= 32 or c >= 127:
        return '.'
    return chr(c)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='hexdump',
        description="prints the hexdump output to stdout",
    )

    parser.add_argument('filename')
    parser.add_argument('-l', '--line-count', type=int)
    parser.add_argument('-o', '--offset', type=int, default=0)

    args = parser.parse_args()
    hexdump(args.filename,
            line_count=args.line_count,
            offset=args.offset)
    return 0


if __name__ == "__main__":
    exit(main())
