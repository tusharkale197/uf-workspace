# Implement a combination of merge insertion sort and record the times
import time
import AOA.sorting_algos as sa


def merge_insertion_sort(input_list, pivot, select_sort):
    """

    :param input_list: The list of numbers that needs sorting
    :param pivot:
    :param select_sort:
    :return: execution times of the mixed
    """
    start_time = time.time()
    insr_time = 0
    mrg_time = 0
    output_list = list()
    if select_sort == 0:

        if len(input_list) <= pivot:
            output_list = sa.insertion_sort(input_list)
            print("Call insertion sort here")
        else:
            print("Call merge sort here")

    elif select_sort == 1:
        mrg_str_time = time.time()
        print("use only merge sort")
        mrg_end_time = time.time()
        mrg_time = mrg_end_time - mrg_str_time

    elif select_sort == 2:
        insr_str_time = time.time()
        print("use only insertion sort")
        insr_end_time = time.time()
        insr_time = insr_end_time - insr_str_time

    end_time = time.time()
    total_time = end_time-start_time
    return output_list, total_time, insr_time, mrg_time


if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    exec_time = merge_insertion_sort(a, 100, 0)

