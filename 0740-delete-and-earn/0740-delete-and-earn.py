class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        range_array = [0] * (max(nums) + 1)
        for num in nums:
            range_array[num] += num
        dp_curr = 0
        dp_prev = 0
        for num in range_array:
            dp_curr, dp_prev = max(dp_curr, dp_prev + num), dp_curr
        return dp_curr