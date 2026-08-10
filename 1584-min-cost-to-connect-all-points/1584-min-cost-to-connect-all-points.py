class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.n = n
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        self.parent[self.find(x)] = self.find(y)
        self.n -= 1
        return True
    def count(self):
        return self.n

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        edges.sort(key = lambda e: e[0])
        uf = UnionFind(n)
        sum_wt = 0
        for d, x, y in edges:
            if uf.union(x, y):
                sum_wt += d
            if uf.count() == 1:
                break
        return sum_wt