class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        n0 = 0
        n1 = 0
        n01 = 0
        n10 = 0
        ans = 0
        for l in s:
            num = int(l)
            n0 += 1 - num
            n1 += num
            n01 += num * n0
            n10 += (1 - num) * n1
            ans += (1 - num) * n01 + num * n10
        return ans