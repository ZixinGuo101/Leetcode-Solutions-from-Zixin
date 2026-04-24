class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = set()
        if k == 0:
            return False

        for r, num in enumerate(nums):
            if num in d:
                return True
            else:
                d.add(num)
            l = r - k
            if l >= 0:
                d.discard(nums[l])
        
        return False
        