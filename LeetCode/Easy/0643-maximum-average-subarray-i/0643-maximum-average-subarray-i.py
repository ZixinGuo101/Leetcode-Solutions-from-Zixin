class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        res = float('-inf')
        s = 0

        for right, num in enumerate(nums):
            s += num

            left = right - k + 1
            if left < 0:
                continue
            
            # print(left, ' ', right)
            
            res = max(res, s)

            s -= nums[left]
            left += 1
        
        return res / float(k)
        