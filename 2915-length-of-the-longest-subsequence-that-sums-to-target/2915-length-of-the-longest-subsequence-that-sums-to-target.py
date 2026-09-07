class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * (target + 1)
        dp[0] = 0
        for num in nums:
            for i in range(target, num-1, -1):
                k = dp[i - num] + 1
                if k < 1:
                    k = -1
                dp[i] = max(dp[i], k)
        return dp[target]
        # for i in range(1, n+1):
        #     num = nums[i-1]
        #     for j in range(target, num - 1, -1):
        #         dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - num] + 1)
        # return dp[n][target] if dp[n][target] != 0 else -1