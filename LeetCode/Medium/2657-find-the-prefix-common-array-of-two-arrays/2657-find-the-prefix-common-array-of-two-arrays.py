
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        countA = 0
        countB = 0
        c = []
        for i in range(len(A)):
            countA |= 1 << A[i]
            countB |= 1 << B[i]
            c.append((countA & countB).bit_count())
        return c