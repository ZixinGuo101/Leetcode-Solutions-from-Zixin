class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        slow = -1
        fast = 0

        while fast < n:
            if nums[fast] != val:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        
        return slow + 1