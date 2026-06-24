class Solution:
    def reverseBits(self, n: int) -> int:
        m1 = 0x55555555
        m2 = 0x33333333
        m3 = 0x0f0f0f0f
        m4 = 0x00ff00ff
        m5 = 0x0000ffff
        d = (n >> 1) & m1 | (n & m1) << 1
        d = (d >> 2) & m2 | (d & m2) << 2
        d = (d >> 4) & m3 | (d & m3) << 4
        d = (d >> 8) & m4 | (d & m4) << 8
        d = (d >> 16) & m5 | (d & m5) << 16
        return d

