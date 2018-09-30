def build_roman_value_dict():

    roman_values = dict()
    roman_values["I"] = 1
    roman_values["V"] = 5
    roman_values["X"] = 10
    roman_values["L"] = 50
    roman_values["C"] = 100
    roman_values["D"] = 500
    roman_values["M"] = 1000

    return roman_values


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    try:
        roman_values = build_roman_value_dict()
        roman_rev = "".join(reversed(s))
        num = 0
        prev_val = 0
        for ind in roman_rev:
            if prev_val > roman_values[ind]:
                add_num = -1 * roman_values[ind]
            else:
                add_num = roman_values[ind]
            prev_val = roman_values[ind]
            num = num + add_num

        print(num)

    except Exception as exc:
        raise exc


if __name__ == "__main__":
    romanToInt("LVIII")