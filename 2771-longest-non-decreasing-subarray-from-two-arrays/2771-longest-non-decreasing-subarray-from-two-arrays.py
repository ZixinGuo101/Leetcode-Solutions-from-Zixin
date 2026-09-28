class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1 = dp2 = 1   # 选 nums1 或 nums2 之后LNDS 的长度
        prev1 = prev2 = min(nums1[0], nums2[0])
        ans = 1
        for i in range(1, n):
            new1_dp1 = dp1 + 1 if nums1[i] >= prev1 else 1
            new2_dp1 = dp2 + 1 if nums1[i] >= prev2 else 1
            new1_dp2 = dp1 + 1 if nums2[i] >= prev1 else 1
            new2_dp2 = dp2 + 1 if nums2[i] >= prev2 else 1
            dp1, dp2 = max(new1_dp1, new2_dp1), max(new1_dp2, new2_dp2)
            ans = max(ans, dp1, dp2)
            prev1 = nums1[i]
            prev2 = nums2[i]
        return ans
