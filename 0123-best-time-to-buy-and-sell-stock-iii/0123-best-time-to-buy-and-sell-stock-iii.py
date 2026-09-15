class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 0 表示无票，1 表示有票
        n = len(prices)
        dp = [[-inf] * 3 for _ in range(2)]
        dp[0][:] = [0] * 3
        for i in range(n):
            for j in range(2, 0, -1):
                dp[0][j] = max(dp[0][j], dp[1][j] + prices[i])
                dp[1][j] = max(dp[1][j], dp[0][j-1] - prices[i])
        return max(dp[0])