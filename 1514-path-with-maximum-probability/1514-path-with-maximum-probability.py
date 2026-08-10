class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        for (a, b), p in zip(edges, succProb):
            g[a].append((p, b))
            g[b].append((p, a))
        s = [0] * n
        s[start_node] = 1
        q = [(-1, start_node)]
        while q:
            p, x = heapq.heappop(q)
            if x == end_node:
                return s[end_node]
            if s[x] > -p:
                continue
            for nxt_p, nxt in g[x]:
                nxt_p *= -p
                if nxt_p > s[nxt]:
                    heapq.heappush(q, (-nxt_p, nxt))
                    s[nxt] = nxt_p
        return s[end_node]