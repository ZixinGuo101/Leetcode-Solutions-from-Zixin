class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]
        n = len(nums)
        cur = nums[0]

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                cur = cur + nums[i]
                res = max(cur, res)
            else:
                cur = nums[i]
        
        return res
        