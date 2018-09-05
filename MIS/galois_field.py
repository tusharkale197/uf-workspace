
def galois_multiplication(first_num, second_num, order):

    """
    :param first_num: First number
    :param second_num: Second Number
    :param order: the order of the galois field table
    :return: Returns the Galois Multiplication table value for the given numbers
    """
    return (first_num * second_num) % order


if __name__ == '__main__':
    # Setting the order to 43 for GF(43)
    order = 43
    mult_table = [[0 for i in range(43)] for i in range(43)]
    # These for loops builds out a multiplication table for GF(43)
    for i in range(43):
        for j in range(43):
            mult_table[i][j] = galois_multiplication(i, j, order)

    # Boolean to check if multiplicative inverse is present in the field
    mult_inverse = False

    # These for loops check if the element in question (i) has a multiplicative inverse in the field itself
    for i in range(43):
        for j in range(43):
            if mult_table[i][j] == 1:
                mult_inverse = True
        if not mult_inverse:
            print("%s has no multiplicative inverse in the field." % i)


