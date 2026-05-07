class FrontMiddleBackQueue(object):
    __slots__ = 'left', 'right'

    '''
    popleft <-- middle ----left---- front <-- append
    popleft <-- back ----right---- middle <-- append
    '''

    def __init__(self):
        self.left = deque()
        self.right = deque()

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.left.append(val)
        if len(self.left) > len(self.right):
            self.right.append(self.left.popleft())
        

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.left) == len(self.right):
            self.right.append(val)
        else:
            self.left.appendleft(val)

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.right.appendleft(val)
        if len(self.left) + 1 < len(self.right):
            self.left.appendleft(self.right.pop())

    def popFront(self):
        """
        :rtype: int
        """
        if len(self.left) > 0:
            val = self.left.pop()
        elif len(self.right) > 0:
            val = self.right.pop()
        else:
            return -1

        if len(self.left) + 1 < len(self.right):
            self.left.appendleft(self.right.pop())
        
        return val

    def popMiddle(self):
        """
        :rtype: int
        """
        if len(self.left) + len(self.right) == 0:
            return -1
        elif len(self.left) == len(self.right):
            return self.left.popleft()
        else:
            return self.right.pop()

    def popBack(self):
        """
        :rtype: int
        """
        if len(self.right) > 0:
            val = self.right.popleft()
        else:
            return -1
        
        if len(self.left) > len(self.right):
            self.right.append(self.left.popleft())        

        return val
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()