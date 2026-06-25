class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for num in encoded:
            first ^= num
            res.append(first)
        return res