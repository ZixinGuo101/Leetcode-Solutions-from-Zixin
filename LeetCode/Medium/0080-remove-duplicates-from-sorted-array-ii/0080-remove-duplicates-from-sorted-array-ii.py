class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 2
        i = 2
        while i < len(nums):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
            i += 1
        
        return k