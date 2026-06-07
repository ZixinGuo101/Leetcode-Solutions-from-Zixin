class StockSpanner(object):

    def __init__(self):
        self.stk = []
        self.cur = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.cur += 1
        while self.stk and self.stk[-1][1] <= price:
            self.stk.pop()
        if self.stk:
            res = self.cur - self.stk[-1][0]
        else:
            res = self.cur
        self.stk.append([self.cur, price])
        return res



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)