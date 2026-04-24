class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        k = 1
        n = len(nums)
        for f in range(1, n):
            if nums[f] == nums[s]:
                continue
            s += 1
            nums[s] = nums[f]
            k += 1
        
        return k
        