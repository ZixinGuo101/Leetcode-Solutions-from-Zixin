class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n-2):
            l = i+1
            r = i+2

            while l < r and r < n:
                if (nums[r] - nums[l]) >= nums[i]:
                    l += 1
                    r += 1
                    continue
                while r < n-1 and (nums[r+1] - nums[l]) < nums[i]:
                    r += 1
                # print(l, r)
                ans += r - l
                l += 1
                if l == r:
                    r += 1
            
        return ans

        