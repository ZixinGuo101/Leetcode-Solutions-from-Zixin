class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = n - 1
        while x < m and y >= 0:
            val = matrix[x][y]
            if val == target:
                return True
            elif val > target:
                y -= 1
            elif val < target:
                x += 1
        
        return False