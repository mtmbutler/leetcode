"""
https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

In a 2 dimensional array grid, each value grid[i][j] represents the
height of a building located there. We are allowed to increase the
height of any number of buildings, by any amount (the amounts can be
different for different buildings). Height 0 is considered to be a
building as well.

At the end, the "skyline" when viewed from all four directions of the
grid, i.e. top, bottom, left, and right, must be the same as the skyline
of the original grid. A city's skyline is the outer contour of the
rectangles formed by all the buildings when viewed from a distance. See
the following example.

What is the maximum total sum that the height of the buildings can be
increased?

Example:
    Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    Output: 35

Explanation:

The grid is:
    [ [3, 0, 8, 4],
      [2, 4, 5, 7],
      [9, 2, 6, 3],
      [0, 3, 1, 0] ]

    The skyline viewed from top or bottom is: [9, 4, 8, 7]
    The skyline viewed from left or right is: [8, 7, 9, 3]

    The grid after increasing the height of buildings without affecting

skylines is:
    gridNew = [ [8, 4, 8, 7],
                [7, 4, 7, 7],
                [9, 4, 8, 7],
                [3, 3, 3, 3] ]

"""


class Solution:

    """Summary
    """

    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Args:
            grid (TYPE): Description

        Returns:
            TYPE: Description
        """

        grid_t = [list(i) for i in zip(*grid)]
        total_max_increase = 0
        for yyy, row in enumerate(grid):
            for xxx, height in enumerate(row):
                comp_y = [i for i in grid[yyy]]
                comp_x = [j for j in grid_t[xxx]]
                max_height = min(max(comp_y), max(comp_x))
                total_max_increase += max_height - height

        return total_max_increase


def main():
    """Summary
    """
    sol = Solution()
    test_cases = [[[3, 0, 8, 4],
                   [2, 4, 5, 7],
                   [9, 2, 6, 3],
                   [0, 3, 1, 0]]]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.maxIncreaseKeepingSkyline(case)))


if __name__ == '__main__':
    main()
