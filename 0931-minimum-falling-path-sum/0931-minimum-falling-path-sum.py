class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0][:]
        if n == 1:
            return min(dp[0])
        ans = float('inf')
        for i in range(1, n):
            for j in range(n):
                mn = dp[i - 1][j]
                if j > 0:
                    mn = min(mn, dp[i - 1][j - 1])
                if j < n - 1:
                    mn = min(mn, dp[i - 1][j + 1])
                dp[i][j] = mn + matrix[i][j]
                if i == n-1 and dp[i][j] < ans:
                    ans = dp[i][j]
        print(dp)
        return ans
