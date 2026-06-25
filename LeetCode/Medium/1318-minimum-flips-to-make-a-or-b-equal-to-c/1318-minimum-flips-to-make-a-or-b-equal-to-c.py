class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        x1 = (a | b) ^ c
        x2 = (a & b) & ~c
        return x1.bit_count() + x2.bit_count()