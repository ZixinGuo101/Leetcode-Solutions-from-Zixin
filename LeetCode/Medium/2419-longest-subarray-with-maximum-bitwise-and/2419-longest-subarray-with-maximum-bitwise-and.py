class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        cnt = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] < maxNum:
                continue
            if nums[i] == maxNum:
                if nums[i] == nums[i-1]:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 1
            if nums[i] > maxNum:
                maxNum = nums[i]
                cnt = 1
                res = 1
        return res