class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mask = 0
        for num in nums:
            d, r = divmod(num, original)
            if r == 0 and d & (d - 1) == 0:
                mask |= d
        mask = ~mask
        return original * (mask & -mask)