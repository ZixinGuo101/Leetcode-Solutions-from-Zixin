class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        if total < abs(target) or (total + target) & 1:
            return 0

        m = (total + target) >> 1
        dp = [0] * (m + 1)
        dp[0] = 1
        for num in nums:
            for i in range(m, num-1, -1):
                dp[i] += dp[i-num]
        return dp[m]
