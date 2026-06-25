class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 1
        i = 0
        j = 1
        pre = nums[0]
        while j < len(nums):
            while j < len(nums) and nums[j] & pre == 0:
                res = max(res, j - i + 1)
                pre |= nums[j]
                j += 1
            if j == len(nums):
                break
            while i < j and nums[j] & pre != 0:
                pre &= ~nums[i]
                i += 1
            pre |= nums[j]
            j += 1
        return res