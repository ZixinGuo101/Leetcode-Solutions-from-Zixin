class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_nums = 0
        max_sum = float('-inf')
        min_sum = float('inf')
        max_include_i = 0
        min_include_i = 0
        for i in range(n):
            sum_nums += nums[i]
            max_include_i = max(max_include_i, 0) + nums[i]
            max_sum = max(max_sum, max_include_i)
            min_include_i = min(min_include_i, 0) + nums[i]
            min_sum = min(min_sum, min_include_i)
        if max_sum <= 0:
            return max_sum
        else:
            return max(max_sum, sum_nums - min_sum)