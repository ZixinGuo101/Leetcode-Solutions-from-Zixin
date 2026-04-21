class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = set()
        left = 0
        
        for right, num in enumerate(nums):
            if num in d:
                return True
            d.add(num)

            if right - left + 1 < k + 1:
                continue
            
            d.discard(nums[left])
            left += 1
        
        return False
        