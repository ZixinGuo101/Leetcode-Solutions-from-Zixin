class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        cnt_0 = 0
        cnt = 0
        left = 0

        for right, num in enumerate(nums):
            if num == 0:
                cnt_0 += 1
            while cnt_0 > k:
                if nums[left] == 0:
                    cnt_0 -= 1
                left += 1
            l = right - left + 1
            res = l if l > res else res
        
        return res
        