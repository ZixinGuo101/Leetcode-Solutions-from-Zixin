class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
        color = [0] * numCourses
        self.no_cycle = True
        def dfs(start):
            if not self.no_cycle:
                return
            if color[start] == 1:
                self.no_cycle = False
                return
            if color[start] == 2:
                return
            color[start] = 1
            for nxt in g[start]:
                if color[nxt] == 2:
                    continue
                dfs(nxt)
            color[start] = 2 
            return
        for i in range(numCourses):
            if self.no_cycle and color[i] == 0:
                dfs(i)
        return self.no_cycle