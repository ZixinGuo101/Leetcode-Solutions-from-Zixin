class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')
        cnt = 0
        left = 0

        for right, num in enumerate(nums):
            cnt += num

            while cnt >= target:
                l = right -left + 1
                ans = l if l < ans else ans
                cnt -= nums[left]
                left += 1
        
        return ans if ans < float('inf') else 0
        