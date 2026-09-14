class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 表示无票，1 表示有票
        dp = [0, -prices[0]]
        n = len(prices)
        for i in range(1, n):
            dp[0] = max(dp[0], dp[1] + prices[i])
            dp[1] = max(dp[1], dp[0] - prices[i])
        return dp[0]