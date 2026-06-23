class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0
        start = (n & -n).bit_length() - 1
        end = start
        n = n >> (start + 1)
        while n:
            end += 1
            if n & 1:
                res = max(res, end - start)
                start = end
            n = n >> 1
        return res