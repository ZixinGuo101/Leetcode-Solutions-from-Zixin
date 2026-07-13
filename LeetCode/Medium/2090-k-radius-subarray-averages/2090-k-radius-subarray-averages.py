class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        if n < (2 * k + 1):
            return res
        total = 0
        for r in range(n):
            total += nums[r]
            if r - 2 * k < 0:
                continue
            res[r - k] = total // (2 * k + 1)
            total -= nums[r - 2 * k]
        return res