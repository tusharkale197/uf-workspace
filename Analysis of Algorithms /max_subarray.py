import math


def max_subarray(input_list, low, high):
    """

    :param input_list: Input list to find a max subarray from
    :param low: the lowest index of input list
    :param high: the highesh index of input list
    :return:
    """
    try:
        # Base case
        if low == high:
            return low, high, input_list[low]
        # recursive step
        else:
            mid = math.floor((high + low)/2)
            # three cases possible here
            # 1. max in ony left (Sub problem of above)
            left_low, left_high, left_max = max_subarray(input_list, low, mid)

            # 2. max in only right (Sub problem of above)
            right_low, right_high, right_max = max_subarray(input_list, mid+1, high)

            # 3. max is on the cross over of both (Have an O(n) implementation for this)
            cross_low, cross_high, cross_max = max_crossing_subarray(input_list, low, high)

        # comparison step
        if left_max >= right_max and left_max >= cross_max:
            return left_low, left_high, left_max
        if right_max >= left_max and right_max >= cross_max:
            return right_low, right_high, right_max
        if cross_max >= right_max and cross_max >= left_max:
            return cross_low, cross_high, cross_max
    except Exception as exc:
        raise exc


def max_crossing_subarray(input_list, low, high):
    """
    FUNCTION TO FIND MAX CROSSING SUBARRAY
    :param input_list:
    :return:
    """

    try:
        size_of_ip = len(input_list)
        mid = math.floor((high+low)/2)

        sum_left = 0
        max_left = -math.inf
        sum_right = 0
        max_right = max_left
        max_right_index = mid
        max_left_index = mid
        for i in range(mid, -1, -1):
            sum_left = sum_left + input_list[i]
            if max_left <= sum_left:
                max_left = sum_left
                max_left_index = i

        for j in range(mid+1, size_of_ip):
            sum_right = sum_right + input_list[j]
            if max_right <= sum_right:
                max_right = sum_right
                max_right_index = j

        max_sum = max_left + max_right

        return max_left_index, max_right_index, max_sum

    except Exception as exc:
        raise exc


if __name__ == "__main__":
    a = [-1, -3,-4]
    print(max_crossing_subarray(a, 0, len(a)-1))
    # print(max_subarray(a, 0, len(a)-1))