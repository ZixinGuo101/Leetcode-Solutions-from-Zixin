class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        path = []
        def dfs(start):
            path.append(start)
            if start == n - 1:
                ans.append(path[:])
                path.pop()
                return
            for nxt in graph[start]:
                dfs(nxt)
            path.pop()
        dfs(0)
        return ans