class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(prices[i] - min_price, dp[i - 1])
            min_price = min(prices[i], min_price)
        return dp[n - 1]