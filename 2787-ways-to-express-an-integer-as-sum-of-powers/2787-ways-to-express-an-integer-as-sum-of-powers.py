class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        modulo = 10 ** 9 + 7
        m = int(n ** (1/x)) + 1
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, m+1):
            r = i ** x
            for j in range(n, r-1, -1):
                dp[j] += dp[j-r]
        return dp[-1] % modulo

















        # m = int(n ** (1/x)) + 1
        # memo = {}

        # def dfs(n, m):
        #     if n == 0:
        #         return 1
        #     if m == 0 or n < 0:
        #         return 0
        #     if (n, m) in memo:
        #         return memo[(n, m)]
        #     return dfs(n - m ** x, m - 1) + dfs(n, m - 1)
        
        # return dfs(n, m) % modulo

            