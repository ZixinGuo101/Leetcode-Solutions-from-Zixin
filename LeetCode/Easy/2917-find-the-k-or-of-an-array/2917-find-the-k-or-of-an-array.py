class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        count = [-k] * 31
        for num in nums:
            while num:
                i = (num & -num).bit_length() - 1
                count[30 - i] += 1
                num &= num - 1
        res = 0
        for c in count:
            if c+1 > 0:
                res = (res << 1) | 1
            else:
                res <<= 1
        return res