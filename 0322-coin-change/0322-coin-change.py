class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = list(set(coin for coin in coins if coin <= amount))
        if not coins:
            return -1
        if len(coins) == 1:
            return amount // coins[0] if amount % coins[0] == 0 else -1
        g = reduce(gcd, coins)
        if amount % g:
            return -1
        if g > 1:
            amount //= g
            coins = [coin // g for coin in coins ]

        mask = (1 << (1 + amount)) - 1
        target = 1 << amount
        seen = 1
        reach = 1
        step = 0
        while reach:
            nxt = 0
            step += 1
            for coin in coins:
                nxt |= reach << coin
            nxt &= mask
            nxt &= ~seen
            if nxt & target:
                return step
            if nxt == 0:
                return -1
            seen |= nxt
            reach = nxt
        return -1

