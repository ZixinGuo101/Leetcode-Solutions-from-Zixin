class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        # if m < n:
        #     return False
        
        memo = {}
        
        def dfs(i, j):
            if i < 0 or j < 0 or i < j:
                return int(j == -1)
            if (i, j) in memo:
                return memo[(i, j)]
            ans = dfs(i - 1, j)
            if s[i] == t[j]:
                ans += dfs(i - 1, j - 1)
            memo[(i, j)] = ans
            return ans

        return dfs(m-1, n-1)