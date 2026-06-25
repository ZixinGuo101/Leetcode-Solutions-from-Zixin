class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        pre = {}
        i0 = False
        for l, c in enumerate(s):
            if c == '0':
                if i0 == False:
                    pre[0] = [l, l]
                    i0 = True
                continue
            x = 0
            for r in range(l, min((l+30), len(s))):
                x = (x << 1) | (ord(s[r]) & 1)
                if x not in pre:
                    pre[x] = [l, r]
        return [pre.get(first ^ second, [-1, -1]) for [first, second] in queries]
