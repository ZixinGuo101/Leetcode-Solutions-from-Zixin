class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(n-1):
            tmp = prices[i+1] - prices[i]
            if tmp > 0:
                profit += tmp
        return profit