#!/bin/python3

import math


# Complete the decentNumber function below.
def decent_number(n):
    if n == 1 or n == 2 or n == 4 or n == 7:
        return -1
    if n % 3 == 0:
        return int('5' * n)
    else:
        for i in range(1, math.ceil(n / 5) + 1):
            if (n - (i * 5)) % 3 == 0:
                return int('5' * (n - (i * 5)) + '3' * (i * 5))


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decent_number(n))