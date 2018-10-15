#!/bin/python3
# https://www.hackerrank.com/challenges/marcs-cakewalk/problem
import math
import os


# Complete the marcsCakewalk function below.
def marcs_cakewalk(calorie):
    # ORDER THEM IN THE DECREASING ORDER OF CALORIES AND CALCULATE CALORIES
    calorie.sort(reverse=True)
    min_miles = 0
    for i in range(0, len(calorie)):
        min_miles = min_miles + pow(2, i) * calorie[i]
    return min_miles


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcs_cakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()

