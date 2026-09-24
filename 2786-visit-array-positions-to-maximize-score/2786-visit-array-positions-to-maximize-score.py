class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        odd = even = -inf
        if nums[0] & 1:
            odd = nums[0]
        else:
            even = nums[0]
        ans = nums[0]
        for i in range(1, n):
            if nums[i] & 1:
                # if odd != 0:
                #     odd += nums[i]
                # if even != 0:
                odd = max(odd + nums[i], even + nums[i] - x) 
                ans = max(ans, odd)
            else:
                # if even != 0:
                #     even = even + nums[i]
                # if odd != 0:
                even = max(even +nums[i], odd + nums[i] - x)
                ans = max(ans, even)
        return ans

