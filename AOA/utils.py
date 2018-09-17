import math

# **** HEAP OPERATIONS **** #


def max_heapify(input_list, element_index, heap_size):
    """
        Function to max heapify a given heap for an element at element_index
    :param input_list:
    :param element_index:
    :param heap_size
    :return:
    """
    try:
        left = left_child(element_index)
        right = right_child(element_index)

        if left <= heap_size and input_list[left] >= input_list[element_index]:
            largest = left
        else:
            largest = element_index

        if right <= heap_size and input_list[right] >= input_list[largest]:
            largest = right

        if largest != element_index:
            input_list[element_index], input_list[largest] = input_list[largest], input_list[element_index]
            max_heapify(input_list, largest, heap_size)

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
            min_heapify(input_list, smallest)

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


def build_max_heap(input_list):
    """
    Given a list this function turns it into a max heap
    :param input_list:
    :return:
    """
    for i in range(math.floor(len(input_list)/2), -1, -1):
        input_list = max_heapify(input_list, i, len(input_list)-1)

    return input_list


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

# **** Quicksort utils****

def partition(input_list, start, end):
    """

    :param input_list: List that needs to be partioned around a pivot
    :param start: Start index of the list
    :param end: End index of the list
    :return: returns the index of the pivot
    """
    try:
        start_pointer = start
        end_pointer = end-1

        # FOLLOWING logic works just fine! Just that the alternate solution is a less complicated implementation of the same strategy
        # while start_pointer < end_pointer:
        #     if input_list[start_pointer] > input_list[end] and input_list[end_pointer] <= input_list[end]:
        #         input_list[start_pointer], input_list[end_pointer] = input_list[end_pointer], input_list[start_pointer]
        #         start_pointer = start_pointer + 1
        #         end_pointer = end_pointer - 1
        #
        #     if input_list[start_pointer] <= input_list[end] and input_list[end_pointer] > input_list[end]:
        #         start_pointer = start_pointer + 1
        #         end_pointer = end_pointer - 1
        #
        #     if input_list[start_pointer] <= input_list[end] and input_list[end_pointer] <= input_list[end]:
        #         start_pointer = start_pointer + 1
        #
        #     if input_list[start_pointer] > input_list[end] and input_list[end_pointer] > input_list[end]:
        #         end_pointer = end_pointer - 1
        # if input_list[start_pointer] <= input_list[end]:
        #     input_list[start_pointer+1], input_list[end] = input_list[end], input_list[start_pointer+1]
        #     pivot_index = start_pointer + 1
        # else:
        #     input_list[start_pointer], input_list[end] = input_list[end], input_list[start_pointer]
        #     pivot_index = start_pointer
        while start_pointer <= end_pointer:
            while input_list[start_pointer] < input_list[end]:
                start_pointer = start_pointer + 1

            while input_list[end_pointer] > input_list[end]:
                end_pointer = end_pointer - 1

            if start_pointer <= end_pointer:
                input_list[start_pointer], input_list[end_pointer] = input_list[end_pointer], input_list[start_pointer]
                start_pointer = start_pointer + 1
                end_pointer = end_pointer - 1

        pivot_index = start_pointer
        input_list[pivot_index], input_list[end] = input_list[end], input_list[pivot_index]
        return pivot_index, input_list

    except Exception as exc:
        raise exc


if __name__ == "__main__":
    b = [15, 3, 2, 1, 9, 5, 7, 8, 6]
    # print(max_heapify(a, 1, len(a)-1))
    print(partition(b, 0, len(b)-1))
