class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l = (n & -n).bit_length()
        if l > 2:
            return False
        n >>= l
        while n:
            gap = (n & -n).bit_length()
            if gap != 2:
                return False
            n >>= gap
        return True