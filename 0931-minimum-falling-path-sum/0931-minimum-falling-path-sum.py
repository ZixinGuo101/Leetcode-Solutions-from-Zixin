class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        for i in range(1, n):
            nxt_dp = [0] * n
            for j in range(n):
                mn = dp[j]
                if j > 0:
                    mn = min(mn, dp[j - 1])
                if j < n - 1:
                    mn = min(mn, dp[j + 1])
                nxt_dp[j] = mn + matrix[i][j]
            dp = nxt_dp
        print(dp)
        return min(dp)
