class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        res = len(nums) + 1
        count = 0
        n = len(nums)
        left = 0
        value = sum(nums) - x

        for right, num in enumerate(nums):
            count += num

            while left <= right and count > value:
                count -= nums[left]
                left += 1
            
            l = right - left + 1
            if count == value and (res == len(nums) + 1 or l > res):
                res = l
        
        return len(nums) - res
        
        

        