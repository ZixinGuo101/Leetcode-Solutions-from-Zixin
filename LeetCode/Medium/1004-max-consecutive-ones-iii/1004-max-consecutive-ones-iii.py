class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt0 = 0
        max_sub = 0
        left = 0

        for right, num in enumerate(nums):
            if num == 0:
                cnt0 += 1
            
            while left <= right and cnt0 > k:
                cnt0 += nums[left] - 1
                left += 1
            
            l = right - left + 1
            max_sub = l if l > max_sub else max_sub
        
        return max_sub
        