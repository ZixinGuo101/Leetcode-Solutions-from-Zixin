class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[-inf] * (n2+1) for _ in range(n1 + 1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = max(nums1[i-1] * nums2[j-1] + max(0, dp[i-1][j-1]), dp[i-1][j], dp[i][j-1])
        # if dp[n1][n2] > 0:
        #     return dp[n1][n2]
        # else:
        #     return max(max(nums1) * min(nums2), min(nums1) * max(nums2))
        return dp[n1][n2]