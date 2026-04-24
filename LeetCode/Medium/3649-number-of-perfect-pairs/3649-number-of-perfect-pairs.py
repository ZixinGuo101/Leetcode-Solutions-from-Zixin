class Solution(object):
    def perfectPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=abs)
        ans = 0
        left = 0

        for i, num in enumerate(nums):
            while abs(nums[left]) * 2 < abs(num):
                left += 1
            ans += i - left
        
        return ans
        