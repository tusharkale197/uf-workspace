# """
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
# """


class Solution(object):

    @staticmethod
    def top_bottom_skyline(grid):
        try:
            top_bottom_skl = list()
            temp = 0
            for i in range(0, len(grid)):
                for j in range(0, len(grid)):
                    if temp < grid[j][i]:
                        temp = grid[j][i]
                top_bottom_skl.append(temp)
                temp = 0
            return top_bottom_skl
        except Exception as exc:
            raise exc

    @staticmethod
    def left_right_skyline(grid):
        try:
            left_right_skl = list()
            temp = 0
            for i in range(0, len(grid)):
                for j in range(0, len(grid)):
                    if temp < grid[i][j]:
                        temp = grid[i][j]
                left_right_skl.append(temp)
                temp = 0
            return left_right_skl

        except Exception as exc:
            raise exc


    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        try:
            grid_len = len(grid)
            grid_new = [[0] * grid_len] * grid_len
            # Calculate top to bottom skyline
            top_bot = self.top_bottom_skyline(grid=grid)

            # Calculate left to right skyline
            left_right = self.left_right_skyline(grid=grid)
            # loop through original to check for max possible increase while keeping track of total increase
            total_change = 0
            for i in range(0, grid_len):
                for j in range(0, grid_len):
                    if left_right[i] <= top_bot[j]:
                        increase = left_right[i] - grid[i][j]
                        total_change = total_change + increase

                    else:
                        increase = top_bot[j] - grid[i][j]
                        total_change = total_change + increase
                    grid_new[i][j] = grid[i][j] + increase
            return total_change
        except Exception as exc:
            raise exc


if __name__ == "__main__":
    sol = Solution()
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(sol.top_bottom_skyline(grid))
    print(sol.left_right_skyline(grid))
    tot_change, grid_new = sol.maxIncreaseKeepingSkyline(grid)

    print(tot_change)
    print(grid_new)
