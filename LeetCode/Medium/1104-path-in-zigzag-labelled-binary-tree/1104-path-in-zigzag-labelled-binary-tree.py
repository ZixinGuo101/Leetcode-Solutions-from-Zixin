class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 1001
        l = label.bit_length()
        tgt = label if l & 1 else (1 << l) - 1 - label + (1 << (l - 1))
        res = []
        path = format(tgt, 'b')
        footprint = 0
        for i in range(len(path)):
            footprint = (footprint << 1) + int(path[i])
            cur = (1 << (i + 1)) - 1 - footprint + (1 << i) if i & 1 else footprint
            res.append(cur)
        return res
        

    