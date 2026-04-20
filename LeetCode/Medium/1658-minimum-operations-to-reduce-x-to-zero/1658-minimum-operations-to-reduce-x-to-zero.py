class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        res = -1
        n = len(nums)
        m = sum(nums) - x
        cnt = 0
        left  = 0

        for right, num in enumerate(nums):
            cnt += num

            while left <= right and cnt - nums[left] >= m:
                cnt -= nums[left]
                left += 1

            if cnt == m:
                l = right - left + 1
                res = l if l > res else res
        
        return n - res if res > -1 else -1

        