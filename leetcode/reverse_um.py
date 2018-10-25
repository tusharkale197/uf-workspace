class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_str = ""
        if x < 0:
            reverse_str = reverse_str + "-"
            x = -1 * (x)
        if x == 0:
            return x
        q = x
        while q != 0:
            reverse_str = reverse_str + str(q%10)
            q = int(q/10)
        rev_int = int(reverse_str)
        if rev_int > 0:
            if rev_int != rev_int & 0x7fffffff:
                return 0
            else:
                return rev_int
        if rev_int < 0:
            if rev_int & -0x80000000 != -2147483648:
                return 0
            else:
                return rev_int


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(-2147483412))
    print(s.reverse(1563847412))

