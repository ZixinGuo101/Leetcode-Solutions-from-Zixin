class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = dict()

        for right, num in enumerate(nums):
            if num in d and right - d[num] <= k:
                return True
            d[num] = right
        
        return False