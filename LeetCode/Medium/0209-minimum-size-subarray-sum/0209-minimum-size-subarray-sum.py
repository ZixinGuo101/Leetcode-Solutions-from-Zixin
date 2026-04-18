class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = float('inf')
        left = 0
        cnt = 0

        for right, num in enumerate(nums):
            cnt += num

            while cnt - nums[left] >= target:
                cnt -= nums[left]
                left += 1
            
            if cnt >= target:
                l = right - left + 1
                res = l if l < res else res
            
        return res if res < float('inf') else 0


        