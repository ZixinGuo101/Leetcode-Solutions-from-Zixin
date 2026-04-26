class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # 0 1 4 4 5 7
        nums.sort()
        ans = 0
        l = len(nums) - 1
        r = len(nums) - 1
        for i, num in enumerate(nums):
            while l > i and nums[l] >= lower - nums[i]:
                l -= 1
            l = l if l > i else i
            while r > l and nums[r] > upper - nums[i]:
                r -= 1
            if r == i:
                break
            ans += r - l
        
        return ans

            
        