class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = 0
        m = n-1

        while m > 1:
            l = 0
            r= m-1
            while l < r:
                if nums[l] + nums[r] > nums[m]:
                    ans += r-l
                    r -= 1
                else:
                    l += 1
            m -= 1
        
        return ans
        