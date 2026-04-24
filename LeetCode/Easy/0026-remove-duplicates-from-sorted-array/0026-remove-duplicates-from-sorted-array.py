class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        f = 1
        k = 1
        while f < len(nums):
            if nums[f] != nums[s]:
                s += 1
                nums[s] = nums[f]
                k += 1
            f += 1
        
        return k