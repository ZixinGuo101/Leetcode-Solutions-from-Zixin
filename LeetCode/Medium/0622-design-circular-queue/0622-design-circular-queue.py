class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [-1] * k
        self.max_len = k
        self.head = 0
        self.rear = 0
        self.len = 0
        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.len == self.max_len:
            return False
        
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.max_len
        self.len += 1
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.len == 0:
            return False
        
        self.head = (self.head + 1) % self.max_len
        self.len -= 1
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.len == 0:
            return -1
        return self.q[self.head]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.len == 0:
            return -1
        
        return self.q[(self.rear + self.max_len - 1) % self.max_len]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.len == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.len == self.max_len
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()