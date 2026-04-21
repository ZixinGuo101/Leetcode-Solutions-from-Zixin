class Solution(object):
    def solve(self, nums, k):
        ans = 0
        left = 0
        cnt1 = 0
        for right, num in enumerate(nums):
            cnt1 += num

            while cnt1 >= k:
                cnt1 -= nums[left]
                left += 1
            
            ans += left
        
        return ans


    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i] = nums[i] & 1
        
        return self.solve(nums, k) - self.solve(nums, k+1)
        
        