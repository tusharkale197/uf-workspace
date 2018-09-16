
def max_heapify(input_list, element_index):
    """
        Function to max heapify a given heap for an element at element_index
    :param input_list:
    :param element_index:
    :return:
    """
    try:
        left = left_child(element_index)
        right = right_child(element_index)
        last_index = len(input_list) - 1

        if left <= last_index and input_list[left] >= input_list[element_index]:
            largest = left
        else:
            largest = element_index

        if right <= last_index and input_list[right] >= input_list[element_index]:
            largest = right

        if largest != element_index:
            input_list[element_index], input_list[largest] = input_list[largest], input_list[element_index]
            max_heapify(input_list, largest)
        return input_list
    except Exception as exc:
        raise exc


def min_heapify(input_list, element_index):
    """
        Function to min heapify a given heap for an element at element_index
    :param input_list:
    :param element_index:
    :return:
    """
    try:
        left = left_child(element_index)
        right = right_child(element_index)
        last_index = len(input_list) - 1

        if left <= last_index and input_list[left] <= input_list[element_index]:
            smallest = left
        else:
            smallest = element_index

        if right <= last_index and input_list[right] <= input_list[element_index]:
            smallest = right

        if smallest != element_index:
            input_list[element_index], input_list[smallest] = input_list[smallest], input_list[element_index]
            max_heapify(input_list, smallest)

        return input_list
    except Exception as exc:
        raise exc


def left_child(element_index):
    """
    Returns the index of the left child of the element at index element_index
    :param element_index:
    :return:
    """

    return (2*element_index) + 1


def right_child(element_index):
    """
    Returns the index of the right child of the element at index element_index
    :param element_index:
    :return:
    """

    return (2*element_index) + 2


# def max_heapify_iter(input_list, element_index):
#     """
# ******* PSUEDOCODE WRITTEN IN THE BOOK. IMPLEMENT IT LATER *******
#         Function to max heapify a given heap for an element at element_index
#     :param input_list:
#     :param element_index:
#     :return:
#     """
#
# try:
#     while j <=
# except Exception as exc:
#     raise exc
if __name__ == "__main__":
    a = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    print(max_heapify(a, 2))
