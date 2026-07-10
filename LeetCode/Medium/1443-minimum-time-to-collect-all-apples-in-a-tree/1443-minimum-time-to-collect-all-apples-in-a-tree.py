class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.graph = {}
        self.visited = set()
        self.visited.add(0)
        for i in range(n):
            self.graph[i] = []
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        
        def dfs(r):
            cur = 0
            for v in self.graph[r]:
                if v not in self.visited:
                    self.visited.add(v)
                    print(v)
                    cur += dfs(v)
                    print(v, cur)
            if r != 0 and (hasApple[r] or cur > 0):
                cur += 2
            return cur
        
        return dfs(0)
