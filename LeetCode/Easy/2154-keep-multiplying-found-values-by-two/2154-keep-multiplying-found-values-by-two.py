class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = p = 0
        for num in nums:
            d, r = divmod(num, original)
            if r == 0 and d & (d - 1) == 0:
                s |= d
        while s & 1:
            p += 1
            s >>= 1
        return original * (2 ** p)