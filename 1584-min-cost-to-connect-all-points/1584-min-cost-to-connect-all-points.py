class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x, y):
            d = abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
            return d
        n = len(points)
        sum_wt = 0
        visited = [False] * n
        q = [(0, 0)]
        while q:
            cur_w, cur_v = heapq.heappop(q)
            if visited[cur_v]:
                continue
            visited[cur_v] = True
            sum_wt += cur_w
            for nxt_v in range(n):
                if not visited[nxt_v]:
                    heapq.heappush(q, (distance(cur_v, nxt_v), nxt_v))
        return sum_wt