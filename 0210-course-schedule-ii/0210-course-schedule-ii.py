class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1
        topo_order = []
        q = [i for i, d in enumerate(in_degree) if d == 0]
        while q:
            cur = q.pop()
            topo_order.append(cur)
            for nxt in graph[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
        return [] if len(topo_order) < numCourses else topo_order