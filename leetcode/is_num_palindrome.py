class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        i = 0
        j = len(x_str)-1
        while j-i >= 1:
            if x_str[i] == x_str[j]:
                j = j-1
                i = i+1
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(-12321))