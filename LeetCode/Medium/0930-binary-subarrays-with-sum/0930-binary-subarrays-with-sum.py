class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """

        def solve(k):
            ans  = 0
            left = 0
            cnt = 0

            for right, num in enumerate(nums):
                cnt += num

                while left <= right and cnt >= k:
                    cnt -= nums[left]
                    left += 1
                
                ans += left
            
            return ans
        
        return solve(goal) - solve(goal+1)

        