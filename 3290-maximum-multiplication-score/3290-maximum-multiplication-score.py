class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        '''
        - 0 1 2 3 4
        0 0 0 0 0 0
        1 0 a 0 0 0
        2 0 b c 0 0
        3 0 d 
        4
        5
        '''
        m = len(b)
        dp = [[0] * 5 for _ in range(m + 1)]
        dp[0][1:] = [-inf] * 4
        for i in range(1, m + 1):
            for j in range(1, 5):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[j - 1] * b[i - 1])
        return dp[m][4]

# class Solution:
#     def maxScore(self, a: List[int], b: List[int]) -> int:
#         n = len(b)
#         f = [[0] * 5 for _ in range(n + 1)]
#         f[0][1:] = [-inf] * 4
#         for i, y in enumerate(b):
#             for j, x in enumerate(a):
#                 f[i + 1][j + 1] = max(f[i][j + 1], f[i][j] + x * y)
#         return f[n][4]