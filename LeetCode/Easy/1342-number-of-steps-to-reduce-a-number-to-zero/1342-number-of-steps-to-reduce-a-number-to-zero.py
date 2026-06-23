class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        num0 = num.bit_length() - num.bit_count()
        num1 = 2 * num.bit_count() - 1
        return num0 + num1