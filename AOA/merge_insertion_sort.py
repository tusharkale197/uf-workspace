# Implement a combination of merge insertion sort and record the times
import time
import AOA.sorting_algos as sa
import random


def merge_insertion_sort(input_list, pivot, select_sort):
    """
    Function to sort elements of a list based on a pivot.
    For smaller size lists insertion sort is used. For list of length > pivot merge sort is used

    :param input_list: The list of numbers that needs sorting
    :param pivot:
    :param select_sort:
    :return: execution times of the mixed
    """
    start_time = time.time()
    output_list = list()
    if select_sort == 0:

        if len(input_list) <= pivot:
            output_list = sa.insertion_sort(input_list)
        else:
            output_list = sa.merge_sort(input_list)

    elif select_sort == 1:

        output_list = sa.merge_sort(input_list)

    elif select_sort == 2:
        output_list = sa.insertion_sort(input_list)

    end_time = time.time()
    total_time = end_time-start_time
    return output_list, total_time


if __name__ == "__main__":
    num_elems = 10000
    my_randoms = [random.randrange(1, num_elems+1, 1) for _ in range(num_elems)]

    op_list, exec_time = merge_insertion_sort(my_randoms, 100, 2)
    print("Insertion sort time")
    print(op_list)
    print(exec_time)

    op_list, exec_time = merge_insertion_sort(my_randoms, 100, 1)
    print("Merge sort time")
    print(op_list)
    print(exec_time)

    op_list, exec_time = merge_insertion_sort(my_randoms, 100, 0)
    print("Merge Insertion sort time")
    print(op_list)
    print(exec_time)