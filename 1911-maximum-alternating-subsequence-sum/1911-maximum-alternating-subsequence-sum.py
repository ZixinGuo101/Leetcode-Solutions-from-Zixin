class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        odd = 0
        even = nums[0]
        n = len(nums)
        ans = nums[0]
        for i in range(1, n):
            odd, even = max(odd, even - nums[i]), max(even, odd + nums[i])
            # ans = max(ans, even)
            # print(odd, even, ans)
        return even