#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the gridChallenge function below.
def gridChallenge(grid):
    prev_ascii= list()
    op = "YES"
    for i in range(0,len(grid)):
        grid[i] = sorted(grid[i])
        count = 0
        for alp in grid[i]:

            if i == 0:
                prev_ascii.append(ord(alp))
            else:
                if prev_ascii[count] > ord(alp):
                    op = "NO"
                prev_ascii[count] = ord(alp)
                count = count + 1

    return op


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)
        print(result)

