def hexdump(in_path: str, /, line_count=20, offset=0):
    """
    takes a filepath and prints the hexdump output to stdout

    Parameters
    ----------
    in_path: str
        the path to the source file to generate the hexdump
    line_count: int
        the number of lines to output
        each line contains 16 Bytes of data
    offset: int
        represents the number of bytes to skip
    Returns
    -------
        None
    Raises
    ------
        IOError
            raised when opening the file errors or __hexdump errors
    """
    with open(in_path, "rb") as in_stream:
        __hexdump(in_stream, line_count, offset)


def __hexdump(inp, line_count, offset):
    """
    takes a filepath and prints the hexdump output to stdout

    Parameters
    ----------
    inp: TextIO
        the StringIO Buffer to the source file to generate the hexdump
    line_count: int
        the number of lines to output
        each line contains 16 Bytes of data
    offset: int
        represents the number of bytes to skip
    Returns
    -------
        None
    Raises
    ------
    IOError
        raised when reading from the file fails or
        printing to stdout in __print_line errors
    """
    inp.seek(offset)

    adr = offset
    line_acc = 0
    while (bs := inp.read(16)) \
            and (True if line_count is None else line_acc < line_count):
        __print_line(adr, bs)

        adr += len(bs)
        line_acc += 1


def __print_line(adr, bs):
    """
    a function to print one line of the hexdump output

    Parameters
    ----------
    adr: int
        the offset of the first Byte in this line
    bs: bytes
        the bytes in this line
        usually has a length of 16, except for the last line
    Returns
    -------
        None
    Raises
    -------
    IOError
        raised when printing to stdout fails
    """
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
    """
    function for conversion from a byte to a ascii value or '.'
    if it is not a representable ascii value

    Parameters
    ----------
    c: int
        the byte to convert to a ascii value
        if the value is larger than the bounds of a ascii codepoint (127)
        a '.' is returned
    Returns
    -------
    chr
        The input interpretet as an ascii value or the '.' Symbol
    """
    if c <= 32 or c >= 127:
        return '.'
    return chr(c)

