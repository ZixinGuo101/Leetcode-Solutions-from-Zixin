class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        acc = -1
        cnt = 0
        for i in range(len(nums)):
            acc &= nums[i]
            if acc == 0:
                cnt += 1
                acc = -1
        return max(cnt, 1)