import math
def insertion_sort(input_list):
    """
        Implementation of Insertion Sort
    :param input_list: List of numbers that needs to be sorted
    :return: Sorted list
    """

    try:
        for j in range(1, len(input_list)):
            temp = input_list[j]
            i = j-1
            while temp < input_list[i] and i >= 0:
                input_list[i+1] = input_list[i]
                i = i-1
            input_list[i+1] = temp
        return input_list
    except Exception as exc:
        raise exc


def merge_sort(input_list):
    """
    Recursive implementaton of merge sort
    :param input_list:
    :param start:
    :param end:
    :return:
    """
    try:

        if len(input_list) <= 1:
            return input_list
        else:
            pivot = math.floor(len(input_list)/2)
            first_half = merge_sort(input_list[:pivot])
            second_half = merge_sort(input_list[pivot:])
        return merge(first_half, second_half)
    except Exception as exc:
        raise exc


def merge(list_1, list_2):
    """
    The MERGE step of merge sort
    :param list_1:
    :param list_2:
    :return: merged sorted list -> a combination of list_1 and list_2
    """
    try:
        i = 0
        j = 0
        m = 0
        merged_list = list()

        while i < len(list_1) and j < len(list_2):
            if list_1[i] <= list_2[j]:
                merged_list.append(list_1[i])
                i = i+1
            else:
                merged_list.append(list_2[j])
                j = j+1

        while i < len(list_1):
            merged_list.append(list_1[i])
            i = i+1
        while j < len(list_2):
            merged_list.append(list_2[j])
            j = j + 1
        return merged_list
    except Exception as exc:
        raise exc


if __name__ == "__main__":
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 8, 10]
    l3 = [3, 6, 11, 2, 7, 0, 1, 44, 6, 3, 78]
    print(merge(l1, l2))
    print(merge_sort(l3))
