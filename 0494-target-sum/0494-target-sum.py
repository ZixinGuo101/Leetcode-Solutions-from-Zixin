class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, c):
            if i < 0:
                return int(c == 0)
            return dfs(i - 1, c + nums[i]) + dfs(i - 1, c - nums[i])
        
        return dfs(n - 1, target)

