class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        dp_earn = nums[0]
        dp_not_earn = 0
        for i in range(1, n):
            temp = max(dp_earn, dp_not_earn)
            if nums[i] == nums[i-1]:
                dp_earn += nums[i]
            elif nums[i] == nums[i-1] + 1:
                dp_earn, dp_not_earn = dp_not_earn + nums[i], temp
            else:
                dp_earn, dp_not_earn = nums[i] + temp, temp
        return max(dp_earn, dp_not_earn)