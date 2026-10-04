class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        ans = nums[0]
        yes0 = yes1 = yes2 = 0
        no1 = no2 = no3 = 0
        for i in range(n):
            if i < n-1:
                yes0, yes1, yes2 = yes1, yes2, nums[i] + max(yes0, yes1)
            if i > 0:
                no1, no2, no3 = no2, no3, nums[i] + max(no1, no2)
            ans = max(ans, yes2, no3)
        return ans