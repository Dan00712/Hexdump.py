import argparse
from hexdump.hexdump import hexdump


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
