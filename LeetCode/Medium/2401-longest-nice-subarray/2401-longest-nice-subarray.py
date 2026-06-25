class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = acc = l = 0
        for r, num in enumerate(nums):
            while acc & num:
                acc ^= nums[l]
                l += 1
            acc |= nums[r]
            ans = max(ans, r - l + 1)
        return ans