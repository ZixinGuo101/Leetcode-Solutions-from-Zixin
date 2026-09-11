class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target) or ((total +target) & 1):
            return 0
        n = len(nums)
        t = (total + target) // 2
        post_sum = [0] * n
        post_sum[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            post_sum[i] = nums[i] + post_sum[i+1]
        # print(post_sum)
        dp = [0] * (t + 1)
        dp[0] = 1
        for i in range(1, n):
            r_bound = max(t - post_sum[i], nums[i-1])
            for j in range(t, r_bound - 1, -1):
                dp[j] += dp[j - nums[i-1]]
            # print(dp)
            # print(r_bound)
        return dp[t] if (t - nums[n-1] < 0) else dp[t] + dp[t - nums[n-1]]