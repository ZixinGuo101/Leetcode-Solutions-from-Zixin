class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        self.cache = dict()
        self.head = Node(-1, -1)
        self.tail = Node(10**4 + 1, 10**5 + 1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            cur = self.cache[key]
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev = self.tail.prev
            cur.next = self.tail
            self.tail.prev.next = cur
            self.tail.prev = cur
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
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            cur.prev = self.tail.prev
            cur.next = self.tail
            self.tail.prev.next = cur
            self.tail.prev = cur
        
        else:
            if len(self.cache) == self.capacity:
                remove = self.head.next
                del self.cache[remove.k]
                self.head.next = remove.next
                remove.next.prev = self.head
                remove.next = None
                remove.prev = None
            
            cur = Node(key, value)
            self.cache[key] = cur
            last = self.tail.prev
            cur.prev = last
            cur.next = self.tail
            last.next = cur
            self.tail.prev = cur




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)