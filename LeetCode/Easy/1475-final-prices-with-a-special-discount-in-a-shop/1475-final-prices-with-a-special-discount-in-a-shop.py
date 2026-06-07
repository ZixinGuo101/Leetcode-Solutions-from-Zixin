class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        ans = [0] * n
        stk = []
        for i in range(n):
            while stk and prices[i] <= prices[stk[-1]]:
                ans[stk[-1]] = prices[stk[-1]] - prices[i]
                stk.pop()
            stk.append(i)
        for i in stk:
            ans[i] = prices[i]
        return ans