class MyQueue(object):

    def __init__(self):
        self.head = []
        self.tail = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.tail.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.head.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if not self.head:
            while self.tail:
                self.head.append(self.tail.pop())
        return self.head[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.head and not self.tail


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()