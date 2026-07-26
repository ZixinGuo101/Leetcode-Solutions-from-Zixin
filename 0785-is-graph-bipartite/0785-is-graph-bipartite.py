class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [False] * len(graph)
        colored = [1] * len(graph)
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    colored[neighbor] = colored[node] ^ 1
                    if not dfs(neighbor):
                        return False
                elif not colored[neighbor] ^ colored[node]:
                        return False
            return True
        for i in range(len(graph)):
            if not dfs(i):
                return False
        return True
