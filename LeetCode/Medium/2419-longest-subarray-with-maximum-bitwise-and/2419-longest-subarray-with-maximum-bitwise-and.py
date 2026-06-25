class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNum = max(nums)
        cnt = ans = 0
        for num in nums:
            if num == maxNum:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans