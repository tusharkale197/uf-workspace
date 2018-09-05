# Implement a combination of merge insertion sort and record the times
import time
def merge_insertion_sort(input_list, pivot, select_sort):

    if select_sort == 0:
        if len(input_list)<=pivot:

            print("Call insertion sort here")
        else:
            print("Call merge sort here")
    elif select_sort == 1:
        print("use only merge sort")
    elif select_sort ==2:
        print("use only insertion sort")

    return

if __name__ == "__main__":

