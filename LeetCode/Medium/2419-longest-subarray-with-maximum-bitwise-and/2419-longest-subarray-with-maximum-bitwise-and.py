class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        cnt = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] < maxNum:
                cnt = 0
            elif nums[i] == maxNum:
                cnt += 1
                res = max(res, cnt)
            else:
                maxNum = nums[i]
                cnt = 1
                res = 1
        return res