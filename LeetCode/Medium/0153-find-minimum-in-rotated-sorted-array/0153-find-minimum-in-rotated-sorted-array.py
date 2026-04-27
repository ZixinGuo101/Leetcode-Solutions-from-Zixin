class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = 1
        r = n - 1

        if nums[0] <= nums[r]:
            return nums[0]
        
        while l <= r:
            mid = l + (r - l) / 2
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        
        return nums[l]