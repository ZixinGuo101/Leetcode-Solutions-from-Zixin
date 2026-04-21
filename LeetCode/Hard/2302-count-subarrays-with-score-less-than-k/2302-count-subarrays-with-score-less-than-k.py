class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pdt = 1
        cnt = 0
        left = 0
        ans = 0

        for right, num in enumerate(nums):
            cnt += num

            pdt = cnt * (right - left + 1)
            while pdt >= k:
                cnt -= nums[left]
                left += 1
                pdt = cnt * (right - left + 1)
            
            ans += right - left + 1
        
        return ans
        
        