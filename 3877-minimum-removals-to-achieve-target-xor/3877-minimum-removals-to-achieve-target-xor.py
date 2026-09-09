class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        # memo = {}
        n = len(nums)

        @cache
        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else inf
            # if (i, c) in memo:
            #     return memo[(i,c)]
            res = min(dfs(i-1, c) + 1, dfs(i-1, c^nums[i]))
            # memo[(i, c)] = res
            return res
        
        ans = dfs(n-1, target)
        return ans if ans != inf else -1