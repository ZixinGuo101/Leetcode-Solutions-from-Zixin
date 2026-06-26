class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float(inf)
        for r, num in enumerate(nums):
            res = min(res, abs(k - num))
            for l in range(r-1, -1, -1):
                if nums[l] | num == nums[l]: # logtrick
                    break
                nums[l] |= num
                res = min(res, abs(k - nums[l]))
        return res
