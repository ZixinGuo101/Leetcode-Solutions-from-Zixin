class Solution:
    def minimumFlips(self, n: int) -> int:
        l = n.bit_length()
        r = 0
        for i in range(l):
            if n & (1 << i):
                r |= 1 << (l - 1 - i)
        return (r ^ n).bit_count()