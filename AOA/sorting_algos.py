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


if __name__ == "__main__":
    a = [4, 3, 2, 1, -2, 6, 9, 10, 27278, 88, 5, 2, 4, 6, 1, 3]
    print(insertion_sort(a))
