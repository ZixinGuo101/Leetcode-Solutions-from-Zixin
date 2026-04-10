class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        n = len(nums)
        new_n = 1
        for fast in range(1, n):
            if nums[fast] == nums[slow]:
                continue
            slow += 1
            nums[slow] = nums[fast]
            new_n += 1
        
        return new_n

        