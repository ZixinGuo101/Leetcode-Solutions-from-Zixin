class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        count = 0
        d = dict()

        for right, num in enumerate(nums):
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            count += num

            left = right - k + 1
            if left < 0:
                continue
            
            if len(d) == k:
                res = max(res, count)
            
            end = nums[left]
            count -= end
            d[end] -= 1
            if d[end] == 0:
                del d[end]
        
        return res

        