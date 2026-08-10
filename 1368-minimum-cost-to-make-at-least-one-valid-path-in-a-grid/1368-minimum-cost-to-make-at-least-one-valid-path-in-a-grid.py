class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        cost = [[float('inf')] * self.col for _ in range(self.row)]
        cost[0][0] = 0
        q = [(0, 0, 0)] # cost, row, col
        while q:
            cur_cost, r, c = heapq.heappop(q)
            if cost[r][c] < cur_cost:
                continue
            for nxt_r, nxt_c, d in self.neighbor(r, c):
                nxt_cost = cur_cost + 1 if d != grid[r][c] else cur_cost
                if cost[nxt_r][nxt_c] > nxt_cost:
                    cost[nxt_r][nxt_c] = nxt_cost
                    heapq.heappush(q, (nxt_cost, nxt_r, nxt_c))
        return cost[self.row - 1][self.col - 1]

    def neighbor(self, r: int, c: int) -> List[int]:
        nei = []
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i, d in enumerate(direction):
            nr = r + d[0]
            nc = c + d[1]
            if nr >= 0 and nr < self.row and nc >= 0 and nc < self.col:
                nei.append((nr, nc, i + 1))
        return nei