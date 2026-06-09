class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = -1
        nmax = nums[0]
        nmin = nums[n-1]
        for i in range(n):
            if nmax > nums[i]:
                end = i
            else:
                nmax = nums[i]
            if nmin < nums[n-1-i]:
                start = n-1-i
            else:
                nmin = nums[n-1-i]
        return end - start + 1
