class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def build(num):
            if num > n:
                return
            res.append(num)
            for i in range(10):
                cur = 10 * num + i
                if cur > n:
                    break
                build(cur)
            return
        for j in range(1, 10):
            build(j)
        return res