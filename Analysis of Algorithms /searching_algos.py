import math


def binary_search(input_list, target_element, low, high):
    """
    Recursive implementation of binary search
    :param input_list:
    :param target_element:
    :return:
    """
    try:

        if high<low:
            return -1
        pivot = math.floor((high+low)/2)
        if target_element == input_list[pivot]:
            return pivot
        if target_element < input_list[pivot]:
            return binary_search(input_list, target_element, low, pivot)
        elif target_element > input_list[pivot]:
            return binary_search(input_list, target_element, pivot+1, high)
    except Exception as exc:
        raise exc


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 7
    print(binary_search(a, x, 0, len(a)-1))