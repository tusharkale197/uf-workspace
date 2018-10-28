import math


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lcp = ""
        index = 0
        len_shortest_str = 0

        for stng in strs:
            if len(stng) < len_shortest_str:
                len_shortest_str = len(stng)
        work = True
        i=0
        while work and i<len_shortest_str:
            temp = strs[0][i]
            for stng in range(0, len(strs)):

                if strs[stng][i] == temp:
                    if stng==len(strs)-1:
                        lcp = lcp + strs[stng][i]
                else:
                    work = False
                    break
            i=i+1
        return lcp


if __name__ == "__main__":
    sol = Solution()
    ip = []
    print(sol.longestCommonPrefix(ip))