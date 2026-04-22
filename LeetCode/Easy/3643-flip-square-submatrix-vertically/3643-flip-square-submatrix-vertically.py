class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """

        lx = x
        ly = y
        rx = x + k - 1
        ry = y

        while lx < rx:
            grid[lx][ly:ly+k], grid[rx][ry:ry+k] = grid[rx][ry:ry+k], grid[lx][ly:ly+k]
            lx += 1
            rx -= 1
        return grid