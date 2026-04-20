class Solution(object):
    def minLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = len(nums) + 1
        left = 0
        cnt = 0
        d = dict()

        for right, num in enumerate(nums):
            if num not in d:
                cnt += num
            d[num] = d.get(num, 0) + 1

            while cnt >= k:
                l = right - left + 1
                ans = l if l < ans else ans
                end = nums[left]
                d[end] -= 1
                if d[end] == 0:
                    del d[end]
                    cnt -= end
                left += 1
        
        if ans == (len(nums) + 1):
            return -1
        return ans