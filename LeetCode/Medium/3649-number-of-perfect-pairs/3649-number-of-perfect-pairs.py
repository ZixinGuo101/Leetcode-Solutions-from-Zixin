class Solution(object):
    def perfectPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [abs(x) for x in nums]
        nums.sort()
        ans = 0
        left = 0

        for i, num in enumerate(nums):
            while nums[left] * 2 < num:
                left += 1
            ans += i - left
        
        return ans
        