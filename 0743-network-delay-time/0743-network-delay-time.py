class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n+1)]
        for u, v, w in times:
            g[u].append((v, w))
        t = [float('inf')] * (n + 1)
        t[0] = t[k] = 0
        q = [(0, k)]
        while q:
            cur_time, cur_node = heapq.heappop(q)
            if t[cur_node] < cur_time:
                continue
            for next_node, next_time in g[cur_node]:
                next_time += cur_time
                if next_time < t[next_node]:
                    t[next_node] = next_time
                    heapq.heappush(q, (next_time, next_node))
        mx = max(t)
        return -1 if mx == float('inf') else mx
