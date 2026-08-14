class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
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

