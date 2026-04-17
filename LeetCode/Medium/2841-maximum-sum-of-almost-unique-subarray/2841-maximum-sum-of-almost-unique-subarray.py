class Solution(object):
    def maxSum(self, nums, m, k):
        """
        :type nums: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        d = {}
        res = 0
        s = 0
        count = 0

        for right, num in enumerate(nums):
            if d.get(num, 0) == 0:
                d[num] = 1
                count += 1
            else:
                d[num] += 1
            s += num

            left = right - k + 1
            if left < 0:
                continue
            
            if count >= m:
                res = max(res, s)
            
            d[nums[left]] -= 1
            if d[nums[left]] == 0:
                count -= 1
            s -= nums[left]
        
        return res



        