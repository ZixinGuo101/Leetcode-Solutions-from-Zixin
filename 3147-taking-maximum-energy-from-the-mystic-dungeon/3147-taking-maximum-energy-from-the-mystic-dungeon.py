class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        if n <= k:
            return max(energy)
        dp = energy[:]
        ans = -inf
        for i in range(k, n):
            dp[i] = max(dp[i], dp[i] + dp[i-k])
        return max(dp[-k:])