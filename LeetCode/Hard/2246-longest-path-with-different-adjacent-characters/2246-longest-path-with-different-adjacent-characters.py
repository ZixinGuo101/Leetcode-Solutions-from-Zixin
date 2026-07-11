class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.graph = [[] for _ in range(len(s))]
        for c in range(1, len(parent)):
            self.graph[parent[c]].append(c)
        self.res = 0
        
        def dfs(root):
            mx = 0
            for child in self.graph[root]:
                n = dfs(child)
                if s[root] != s[child]:
                    self.res = max(self.res, mx + n + 1)
                    mx = max(mx, n)
            return 1 + mx
        
        
        return max(dfs(0), self.res)