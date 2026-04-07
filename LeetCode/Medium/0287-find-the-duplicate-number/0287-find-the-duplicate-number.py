class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 3 1 3 4 2
        # 0 1 2 3 4

        slow = nums[0]
        fast = nums[slow]


        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow



        