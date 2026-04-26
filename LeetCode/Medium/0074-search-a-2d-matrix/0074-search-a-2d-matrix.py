class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def trans(idx):
            i, j = divmod(idx, n)
            return matrix[i][j]
        
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = l + (r - l) / 2
            mm = trans(mid)
            if mm == target:
                return True
            elif mm > target:
                r = mid - 1
            elif mm < target:
                l = mid + 1
        
        return False