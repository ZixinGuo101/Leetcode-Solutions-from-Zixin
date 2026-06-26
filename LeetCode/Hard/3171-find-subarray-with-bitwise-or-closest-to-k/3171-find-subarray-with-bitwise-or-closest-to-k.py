class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 滑动窗口 + 双栈
        res = float(inf)
        right_OR = left = bottom = 0
        for right, num in enumerate(nums):
            right_OR |= num
            while left <= right and right_OR | nums[left] > k:
                res = min(res, (right_OR | nums[left]) - k)
                left += 1
                if left > bottom:
                    for i in range(right - 1, left - 1, -1):
                        nums[i] |= nums[i+1]
                    bottom = right
                    right_OR = 0
            if left <= right:
                res = min(res, k - (right_OR | nums[left]))
            if res == 0:
                break
        return res