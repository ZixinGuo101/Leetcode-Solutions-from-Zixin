class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.parent = [i for i in range(n)]
        self.count = n
        for i in range(1, n):
            for j in range(i):
                if isConnected[j][i]:
                    self.union(i, j)
        return self.count
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        self.parent[rootX] = rootY
        self.count -= 1
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]