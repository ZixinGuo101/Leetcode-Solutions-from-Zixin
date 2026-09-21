class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        ones = 0
        zeros = 0
        zero_ones = 0
        one_zeros = 0

        for c in s:
            if c == '0':
                zeros += 1          # 0
                one_zeros += ones   # 10
                ways += zero_ones   # 010
            else:
                ones += 1           # 1
                zero_ones += zeros  # 01
                ways += one_zeros
        return ways