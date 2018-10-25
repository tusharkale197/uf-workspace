# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1 = self.convert_list_to_num(l1)
        num_2 = self.convert_list_to_num(l2)
        num_sum = num_1 + num_2
        return self.convert_num_to_list(num_sum)

    def convert_list_to_num(self, l):
        """
        :type l: ListNode
        :rtype: integer
        """
        num_str = ""

        while True:
            if not l:
                break
            else:
                num_str = num_str + str(l.val)
                l = l.next
        num_str = num_str[::-1]
        return int(num_str)

    def convert_num_to_list(self, num):
        """
        :type num: integer
        :rtype: ListNode
        """
        num_str = str(num)[::-1]
        l = ListNode(0)
        first = True
        l1 = ListNode(0)
        num_str_len = len(num_str)
        count = 0
        print(num_str)
        for ch in num_str:
            count = count + 1
            if first:
                l.val = int(ch)
                if count < num_str_len:
                    l.next = l1
                first = False
            else:

                l2 = ListNode(0)
                l1.val = int(ch)
                if count < num_str_len:
                    l1.next = l2
                    l1 = l2

        return l


