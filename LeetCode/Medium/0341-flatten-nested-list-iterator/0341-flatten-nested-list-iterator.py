# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stk = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stk.append(nestedList[i])
    
    def next(self) -> int:
        return self.stk.pop().getInteger()
        
    
    def hasNext(self) -> bool:
        while self.stk and not self.stk[-1].isInteger():
            cur = self.stk.pop().getList()
            for i in range(len(cur) - 1, -1, -1):
                self.stk.append(cur[i])
        return bool(self.stk)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())