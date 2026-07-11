class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        graph1 = [[] for _ in range(len(edges1) + 1)]
        graph2 = [[] for _ in range(len(edges2) + 1)]
        for s, e in edges1:
            graph1[s].append(e)
            graph1[e].append(s)
        for s, e in edges2:
            graph2[s].append(e)
            graph2[e].append(s)
        self.res = 0

        def maxDiameter(node, parent, graph):
            total = 0
            mx = 0
            for child in graph[node]:
                if child == parent:
                    continue
                child_diameter = maxDiameter(child, node, graph)
                self.res = max(self.res, mx + child_diameter)
                mx = max(mx, child_diameter)
            return mx + 1
        
        maxDiameter(0, -1, graph1)
        d1, self.res = self.res, 0
        maxDiameter(0, -1, graph2)
        d2, self.res = self.res, 0
        return max(int((d1 + 1) / 2) + int((d2 + 1) / 2) + 1, max(d1, d2))

