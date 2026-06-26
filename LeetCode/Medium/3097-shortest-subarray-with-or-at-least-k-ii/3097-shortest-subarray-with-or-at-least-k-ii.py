class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float(inf)
        for right, num in enumerate(nums):
            if num >= k:
                res = 1
            if res == 1:
                return res
            for left in range(right - 1, -1, -1):
                if nums[left] | num == nums[left]:
                    break
                nums[left] |= nums[left+1]
                if nums[left] >= k:
                    res = min(res, right - left + 1)
                    break
        return res if res < float(inf) else -1