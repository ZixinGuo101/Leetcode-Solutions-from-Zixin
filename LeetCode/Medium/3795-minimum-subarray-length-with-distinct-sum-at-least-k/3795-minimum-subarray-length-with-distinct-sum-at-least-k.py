class Solution(object):
    def minLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = float('inf')
        left = 0
        l = float('inf')
        cnt = 0
        d = dict()
        for right, num in enumerate(nums):
            if num not in d:
                cnt += num
            d[num] = d.get(num, 0) + 1

            while cnt >= k:
                end = nums[left]
                if d[end] == 1:
                    cnt -= end
                    del d[end]
                else:
                    d[end] -= 1
                l = right - left + 1
                res = l if l < res else res
                left += 1
            
            
            

        if res == float('inf'):
            return -1
        else:
            return res