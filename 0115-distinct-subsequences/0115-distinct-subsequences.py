class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m < n:
            return 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i, m + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1] if i != 1 else 1
                dp[i][j] += dp[i][j - 1]
        # for d in dp:
        #     print(d)
        return dp[n][m]