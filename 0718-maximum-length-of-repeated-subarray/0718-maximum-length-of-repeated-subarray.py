class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        ans = 0
        for i in range(1, n2+1):
            for j in range(1, n1+1):
                if nums2[i-1] == nums1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(ans, dp[i][j])

        # for l in dp:
        #     print(l)
        return ans