class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        d = dict()

        for r, num in enumerate(nums):
            idx = num / (valueDiff+1)
            if idx in d:
                return True
            if idx-1 in d and abs(d[idx-1] - num) <= valueDiff:
                return True
            if idx+1 in d and abs(d[idx+1] - num) <= valueDiff:
                return True
            
            d[idx] = num
            
            l = r - indexDiff
            if l >= 0:
                del d[nums[l] / (valueDiff+1)]
        
        return False
        