class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = 0
        m = n - 1

        while m > 1:
            l = 0
            r = m - 1
            while l < r:
                while l < r and nums[l] + nums[r] <= nums[m]:
                    l += 1
                if l < r:
                    ans += r - l
                r -= 1
            m -= 1
        
        return ans
        