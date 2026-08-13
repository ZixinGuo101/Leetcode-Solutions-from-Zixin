class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for money in range(1, len(dp)):
            for coin in coins:
                if money < coin:
                    continue
                dp[money] = min(dp[money], dp[money - coin] + 1)
        return dp[-1] if dp[-1] < amount + 1 else -1