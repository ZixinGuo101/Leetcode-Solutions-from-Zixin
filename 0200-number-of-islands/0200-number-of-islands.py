class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(x, y):
            for d in direction:
                nx = x + d[0]
                ny = y + d[1]
                if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[ny][nx]:
                    visited[ny][nx] = True
                    if grid[ny][nx] == '1':
                        dfs(nx, ny)
            return
        
        for x in range(n):
            for y in range(m):
                if not visited[y][x]:
                    visited[y][x] = True
                    if grid[y][x] == '1':
                        ans += 1
                        dfs(x, y)
        
        return ans


        