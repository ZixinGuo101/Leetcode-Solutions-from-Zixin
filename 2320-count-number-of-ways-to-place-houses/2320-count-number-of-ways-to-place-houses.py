class Solution:
    def countHousePlacements(self, n: int) -> int:
        yes = 0
        no = 1
        for i in range(n):
            yes, no = no, yes + no
        return (yes + no) ** 2 % (10 ** 9 + 7)