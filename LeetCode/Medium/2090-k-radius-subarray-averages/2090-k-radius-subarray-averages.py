class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        if len(nums) < (2*k+1):
            return res
        
        count = 0
        for right, num in enumerate(nums):
            count += num

            left = right - 2*k
            if left < 0:
                continue
            
            res[right-k] = int(count//(2*k+1))

            count -= nums[left]
            left += 1
        
        return res
        