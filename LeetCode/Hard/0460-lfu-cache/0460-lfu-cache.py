class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.f = 1
        self.head = None
        self.prev = None

class LinkedHashSet:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        x.prev = None
        x.next = None
    
    def removeFirst(self):
        d = self.head.next
        self.head.next = d.next
        d.next.prev = self.head
        d.next = None
        d.prev = None

        return d

    def add(self,x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
    
    def isEmpty(self):
        if self.head.next == self.tail:
            return True
        else:
            return False
    
    def out(self):
        p = self.head.next
        while p != self.tail:
            print(p.k, p.v)
            p = p.next

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.freq = dict()
        self.min_freq = 0
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        cur = self.cache[key]
        curSet = self.freq[cur.f]
        curSet.remove(cur)
        if curSet.isEmpty():
            del self.freq[cur.f]
            if self.min_freq == cur.f:
                self.min_freq += 1
        cur.f += 1
        if cur.f not in self.freq:
            self.freq[cur.f] = LinkedHashSet()
        self.freq[cur.f].add(cur)
        
        # print("after get", self.min_freq)
        # print(self.freq[self.min_freq].out())
        return cur.v
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            cur = self.cache[key]
            cur.v = value
            self.freq[cur.f].remove(cur)
            if self.freq[cur.f].isEmpty():
                if self.min_freq == cur.f:
                    self.min_freq += 1
                del self.freq[cur.f]
            cur.f += 1
            if cur.f not in self.freq:
                self.freq[cur.f] = LinkedHashSet()
            self.freq[cur.f].add(cur)
        
        else:
            if len(self.cache) == self.capacity:
                curSet = self.freq[self.min_freq]
                d = curSet.removeFirst()
                del self.cache[d.k]
                if curSet.isEmpty():
                    del self.freq[self.min_freq]
            cur = Node(key, value)
            self.cache[key] = cur
            if 1 not in self.freq:
                self.freq[1] = LinkedHashSet()
            self.freq[1].add(cur)
            self.min_freq = 1
        # print("after put:")
        # print(self.freq[1].out())

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)