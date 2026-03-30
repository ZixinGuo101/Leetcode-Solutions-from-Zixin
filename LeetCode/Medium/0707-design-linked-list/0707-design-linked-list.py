class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0


    def get(self, index: int) -> int:
        if index <0 or index >= self.size:
            return -1
        p = self.head.next
        for i in range(index):
            p = p.next
        return p.val
        

    def addAtHead(self, val: int) -> None:
        p = Node(val)
        p.next = self.head.next
        p.prev = self.head
        self.head.next.prev = p
        self.head.next = p
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        p = Node(val)
        p.next = self.tail
        p.prev = self.tail.prev
        self.tail.prev.next = p
        self.tail.prev = p
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        p = Node(val)
        j = self.head.next
        for i in range(index):
            j = j.next
        p.next = j
        p.prev = j.prev
        j.prev.next = p
        j.prev = p
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        j = self.head.next
        for i in range(index):
            j = j.next
        # toDelete = j
        j.prev.next = j.next
        j.next.prev = j.prev
        j.prev = None
        j.next = None
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)