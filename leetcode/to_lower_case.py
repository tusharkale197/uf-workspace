def toLowerCase(str):
    """
    :type str: str
    :rtype: str
    """
    str = list(str)
    op_str = ""
    for s in str:
        ascii_s = ord(s)
        if 90 >= ascii_s >= 65:
            ascii_s = ascii_s + 32
            op_str = op_str + chr(ascii_s)
        else:
            op_str = op_str + s
    return op_str


if __name__ == "__main__":
    print(toLowerCase("Hello"))


