class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        sums = 0
        for num in nums:
            sums = max(sums, 0) + num
            res = max(sums, res)
        return res