class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total & 1:
            return False
        total >>= 1
        dp = 1
        for num in nums:
            dp |= dp << num
            if dp & (1 << total):
                return True
        return False