class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        pdt = 1
        res = 0

        for right, num in enumerate(nums):
            pdt = pdt * num

            while left <= right and pdt >= k:
                pdt = pdt / nums[left]
                left += 1
            
            res += right - left + 1
        
        return res