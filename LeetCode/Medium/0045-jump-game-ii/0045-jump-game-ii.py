class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [n] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            step = nums[i]
            if nums[i] == 0:
                continue
            cur = [dp[idx] for idx in range(i+1, i+step+1) if idx < n]
            # print(cur)
            dp[i] = min(cur) + 1
        
        return dp[0]

        