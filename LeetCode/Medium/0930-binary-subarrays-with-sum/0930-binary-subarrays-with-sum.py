class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        d = {0:1}
        pre_sum = 0
        n = len(nums)
        ans = 0

        for i in range(n):
            pre_sum += nums[i]

            if pre_sum - goal in d:
                ans += d[pre_sum-goal]
            d[pre_sum] = d.get(pre_sum, 0) + 1
        
        return ans
        