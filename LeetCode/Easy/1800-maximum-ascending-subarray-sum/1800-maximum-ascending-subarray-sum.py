class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = 1
        cnt = nums[0]
        max_cnt = nums[0]

        while right < n:
            if nums[right] > nums[right - 1]:
                cnt += nums[right]
                max_cnt = cnt if max_cnt < cnt else max_cnt
            else:
                left = right
                cnt = nums[left]
            
            right += 1
        
        return max_cnt

        