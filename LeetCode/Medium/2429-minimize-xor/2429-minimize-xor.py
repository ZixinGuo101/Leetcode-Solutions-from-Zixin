class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        l1 = num1.bit_length()
        c2 = num2.bit_count()
        x = 0
        while c2 and l1:
            if num1 & (1 << (l1 - 1)):
                x |= 1 << (l1 - 1)
                c2 -= 1
            l1 -= 1
        i = 0
        while c2:
            if x & (1 << i) == 0:
                x |= (1 << i)
                c2 -= 1
            i += 1
        return x