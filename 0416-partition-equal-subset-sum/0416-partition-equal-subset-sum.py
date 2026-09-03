class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        total //= 2
        @cache
        def dfs(i, c):
            if i < 0:
                return c == 0
            if nums[i] > c:
                return dfs(i - 1, c)
            return dfs(i - 1, c) or dfs(i - 1, c - nums[i])
        if dfs(n - 1, total):
            return True
        else:
            return False