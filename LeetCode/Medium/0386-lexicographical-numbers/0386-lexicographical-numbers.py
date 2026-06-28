class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # 1, 10, 100, 101, 102,..., 109, 11, 110, 111, 112, 113, 114, ..., 119, 12, 120
        res = []
        candidates = [0]
        while candidates:
            curr = candidates.pop()
            if curr > 0:
                res.append(curr)
            for i in range(9, -1, -1):
                if curr+i == 0:
                    continue
                if curr * 10 + i <= n:
                    candidates.append(curr * 10 + i)
        return res
        return res