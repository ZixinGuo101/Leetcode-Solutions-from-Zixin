class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x, y):
            d = abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
            return d
        n = len(points)
        total = 0
        min_dist = [float('inf')] * n
        remaining = set([i for i in range(n)])
        cur = 0
        remaining.remove(cur)
        min_dist[cur] = 0
        while remaining:
            best_v = -1
            best_d = float('inf')
            for v in remaining:
                d = distance(cur, v)
                if d < min_dist[v]:
                    min_dist[v] = d
                if min_dist[v] < best_d:
                    best_d = min_dist[v]
                    best_v = v
            if best_v == -1:
                return -1
            total += best_d
            cur = best_v
            remaining.remove(cur)
        return total