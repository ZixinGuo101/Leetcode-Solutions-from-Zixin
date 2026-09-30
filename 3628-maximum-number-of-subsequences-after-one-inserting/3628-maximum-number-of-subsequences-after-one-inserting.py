class Solution:
    def numOfSubsequences(self, s: str) -> int:
        t = s.count('T')
        l = lc = lct = c = ct = lt = 0
        for b in s:
            if b == 'L':
                l += 1
            elif b == 'C':
                lc += l
                c += 1
            elif b == 'T':
                lct += lc
                ct += c
                t -= 1
            lt = max(lt, l * t)
        return lct + max(ct, lc, lt)