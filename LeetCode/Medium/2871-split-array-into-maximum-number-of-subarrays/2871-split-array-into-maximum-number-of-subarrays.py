class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        maxNum = (1 << (10 ** 6).bit_length()) - 1
        acc = m = maxNum
        cnt = 0
        for i in range(len(nums)):
            m &= nums[i]
            acc &= nums[i]
            if acc == 0:
                cnt += 1
                acc = maxNum
        return 1 if m else cnt