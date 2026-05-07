class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [-1] * k
        self.max_len = k
        self.front = 0
        self.rear = 0
        self.len = 0
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        self.len += 1
        self.front = (self.front + self.max_len - 1) % self.max_len
        self.q[self.front] = value
        return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        self.len += 1
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.max_len
        return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max_len
        self.len -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear + self.max_len - 1) % self.max_len
        self.len -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        
        return self.q[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
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
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()