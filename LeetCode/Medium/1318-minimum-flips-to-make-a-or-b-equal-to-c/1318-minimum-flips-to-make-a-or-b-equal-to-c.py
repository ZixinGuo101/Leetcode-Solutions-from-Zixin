class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        mask = (a | b) ^ c
        res = 0
        while mask:
            t = mask & -mask
            print(bin(t))
            if t & c == 0:
                res += 2 if a & b & t else 1
            else:
                res += 1
            mask &= mask - 1
            print(res)
        return res