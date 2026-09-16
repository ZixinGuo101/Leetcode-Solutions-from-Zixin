class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        # 状态：第i天进行最多j次交易后是否有票，0表示无票，1表示有票
        # dp[i][j][2]
        n = len(prices)
        # dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0][1] = -inf
        # for i in range(k+1):
        #     dp[0][i][1] = -inf
        # for i in range(1, n+1):
        #     for j in range(1, k+1):
        #         dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i-1])
        #         dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i-1])
        # return dp[n][k][0]

        dp = [[0, -inf] for _ in range(k+1)]    # 初始化按照第0天来做
        for i in range(n):
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i])
        return dp[k][0]
