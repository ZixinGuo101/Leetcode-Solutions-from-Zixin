class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False
        total >>= 1
        dp = [[False] * (total + 1) for _ in range(n + 1)]
        dp[0][0] = True
        temp_sum = 0
        for i in range(1, n + 1):
            x = nums[i - 1]
            temp_sum += x
            for j in range(1, total + 1):
                if j > temp_sum:
                    break
                dp[i][j] = dp[i - 1][j]
                if j >= x:
                    dp[i][j] |= dp[i - 1][j - x]
        return dp[n][total]