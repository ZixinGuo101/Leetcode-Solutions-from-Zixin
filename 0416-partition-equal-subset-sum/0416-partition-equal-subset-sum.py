class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False
        total >>= 1
        dp = [False] * (total + 1)
        dp[0] = True
        temp_sum = 0
        for num in nums:
            temp_sum += num
            end = min(temp_sum, total)
            for i in range(end, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[total]