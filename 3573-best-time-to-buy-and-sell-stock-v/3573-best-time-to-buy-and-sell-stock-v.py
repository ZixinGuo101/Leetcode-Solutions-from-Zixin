class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        # 状态：第i天进行了最多j笔交易之后，手里是0无票，1有票，2欠票
        n = len(prices)
        # dp = [[[0] * 3 for _ in range(k+1)] for _ in range(n+1)]
        # for j in range(k+1):
        #     dp[0][j][1] = dp[0][j][2] = -inf
        # for i in range(n+1):
        #     dp[i][0][1] = dp[i][0][2] = -inf
        # for i in range(1, n+1):
        #     for j in range(1, k+1):
        #         dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][2] - prices[i-1], dp[i-1][j][1] + prices[i-1])
        #         dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i-1])
        #         dp[i][j][2] = max(dp[i-1][j][2], dp[i-1][j-1][0] + prices[i-1])
        # return dp[n][k][0]

        dp = [[0, -inf, -inf] for _ in range(k+1)]
        for p in prices:
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][2] - p, dp[j][1] + p)
                dp[j][1] = max(dp[j][1], dp[j-1][0] - p)
                dp[j][2] = max(dp[j][2], dp[j-1][0] + p)
        return dp[k][0]