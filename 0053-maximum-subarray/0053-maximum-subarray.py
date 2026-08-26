class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur = nums[0]
        prev = 0
        ans = cur
        for i in range(1, n):
            prev = cur
            cur = prev + nums[i] if prev > 0 else nums[i]
            ans = max(ans, cur)
        return ans