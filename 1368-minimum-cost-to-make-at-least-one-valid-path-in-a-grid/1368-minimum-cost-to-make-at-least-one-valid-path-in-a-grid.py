class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        cost = [[float('inf')] * self.col for _ in range(self.row)]
        cost[0][0] = 0
        q = deque([(0, 0)]) # row, col
        visited = [[False] * self.col for _ in range(self.row)]
        while q:
            r, c = q.popleft()
            if visited[r][c]:
                continue
            visited[r][c] = True
            for nr, nc, d in self.neighbor(r, c):
                new_cost = cost[r][c] + 1 if d != grid[r][c] else cost[r][c]
                if new_cost < cost[nr][nc]:
                    cost[nr][nc] = new_cost
                    if d == grid[r][c]:
                        q.appendleft((nr, nc))
                    else:
                        q.append((nr, nc))
        return cost[self.row - 1][self.col - 1]
    
    def neighbor(self, r, c):
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ans = []
        for i, d in enumerate(direction):
            nr = r + d[0]
            nc = c + d[1]
            if nr >= 0 and nr < self.row and nc >= 0 and nc < self.col:
                ans.append((nr, nc, i + 1))
        return ans
