class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = [-1] * len(graph)
        def dfs(node, c):
            colored[node] = c
            for neighbor in graph[node]:
                if colored[neighbor] == -1:
                    if not dfs(neighbor, colored[node] ^ 1):
                        return False
                elif not colored[neighbor] ^ colored[node]:
                        return False
            return True
        for i in range(len(graph)):
            if colored[i] == -1 and not dfs(i, 0):
                return False
        return True
