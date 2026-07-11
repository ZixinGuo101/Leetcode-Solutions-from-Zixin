class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.graph = [[] for _ in range(len(s))]
        for c in range(1, len(parent)):
            self.graph[parent[c]].append(c)
        self.res = 0
        
        def dfs(root):
            mx1 = mx2 = 0
            for child in self.graph[root]:
                n = dfs(child)
                if s[root] != s[child]:
                    if n > mx2:
                        mx1, mx2 = max(mx1, n), min(mx1, n)
            self.res = max(self.res, 1 + mx1 + mx2)
            return 1 + max(mx1, mx2)
        
        dfs(0)
        return self.res