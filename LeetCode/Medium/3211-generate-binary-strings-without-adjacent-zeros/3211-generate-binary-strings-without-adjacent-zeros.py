class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        mask = (1 << n) - 1
        for num in range(1 << n):
            if num & (num >> 1) == 0:
                res.append(format(num ^ mask, 'b').zfill(n))
        return res