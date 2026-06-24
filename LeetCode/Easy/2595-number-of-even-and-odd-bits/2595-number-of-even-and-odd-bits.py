class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        l = n.bit_length()
        even_mask = 0
        odd_mask = 0
        while l > 0:
            even_mask = (even_mask << 2) | 1
            odd_mask = (odd_mask << 2) | 2
            l -= 2
        return (even_mask & n).bit_count(), (odd_mask & n).bit_count()