class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        self.count = n
        self.parent = [i for i in range(n)]
        for i in range(n):
            if not (self.merge(i, leftChild[i]) and self.merge(i, rightChild[i])):
                return False
        return self.count == 1
    
    def merge(self, i, j):
        if j == -1:
            return True
        if self.parent[j] != j:
            return False
        root_i = self.find(i)
        if root_i == j:
            return False
        self.parent[j] = root_i
        self.count -= 1
        print(self.parent[j])
        return True
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
