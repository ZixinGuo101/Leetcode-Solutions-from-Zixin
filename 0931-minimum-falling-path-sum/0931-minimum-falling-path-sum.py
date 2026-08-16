class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix[0][:]
        for i in range(1, n):
            nxt_dp = [0] * n
            nxt_dp[0] = matrix[i][0] + min(dp[0], dp[1])
            for j in range(1, n - 1):
                nxt_dp[j] =matrix[i][j] + min(dp[j-1], dp[j], dp[j+1])
            nxt_dp[-1] = matrix[i][-1] + min(dp[-1], dp[-2])
            dp = nxt_dp
        print(dp)
        return min(dp)
