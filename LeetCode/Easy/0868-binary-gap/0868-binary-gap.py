class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        n = n >> (n & -n).bit_length()
        while n:
            gap = (n & -n).bit_length()
            res = max(res, gap)
            n = n >> gap
        return res