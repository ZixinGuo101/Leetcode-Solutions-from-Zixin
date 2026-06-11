class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = float('-inf')
        min_sum = 0
        pre_sum = [0] * (n+1)
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
            res = max(res, pre_sum[i] - min_sum)
            if pre_sum[i] < min_sum:
                min_sum = pre_sum[i]
        return res