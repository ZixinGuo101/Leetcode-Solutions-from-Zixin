class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # n = len(prices)
        # dp = [[0] * 3 for _ in range(n+1)]
        # dp[0][1] = dp[0][2] = -inf
        # for i in range(1, n+1):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i-1])
        #     dp[i][2] = dp[i-1][1] + prices[i-1]
        # # for l in dp:
        # #     print(l)
        # return max(dp[n][0], dp[n][2])

        sold = 0
        hold = rest = -inf
        for p in prices:
            prev_sold = sold
            sold = max(prev_sold, rest)
            rest = hold + p
            hold = max(hold, prev_sold - p)
        return max(sold, rest)