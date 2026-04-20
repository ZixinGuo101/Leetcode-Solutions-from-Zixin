class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        
        cnt = 0
        pdt = 1
        left = 0

        for right, num in enumerate(nums):
            pdt *= num

            while left <= right and pdt >= k:
                pdt = pdt / nums[left]
                left += 1
            
            cnt += right - left + 1
        
        return cnt
            

        