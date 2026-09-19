class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        hold = -inf
        sold = 0
        for p in prices:
            prev_sold = sold
            sold = max(prev_sold, hold + p)
            hold = max(hold, prev_sold - p - fee)
        return sold