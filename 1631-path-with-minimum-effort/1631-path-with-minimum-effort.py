class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        effort = [[float('inf')] * col for _ in range(row)]
        effort[0][0] = 0
        q = [(0, 0, 0)] # (effort, row, col)
        while q:
            e, r, c = heapq.heappop(q)
            if effort[r][c] < e:
                continue
            if r < row - 1:
                nxt_e = max(e, abs(heights[r + 1][c] - heights[r][c]))
                if nxt_e < effort[r + 1][c]:
                    heapq.heappush(q, (nxt_e, r + 1, c))
                    effort[r + 1][c] = nxt_e
            if c < col - 1:
                nxt_e = max(e, abs(heights[r][c + 1] - heights[r][c]))
                if nxt_e < effort[r][c + 1]:
                    heapq.heappush(q, (nxt_e, r, c + 1))
                    effort[r][c + 1] = nxt_e
            if r > 0:
                nxt_e = max(e, abs(heights[r - 1][c] - heights[r][c]))
                if nxt_e < effort[r - 1][c]:
                    heapq.heappush(q, (nxt_e, r - 1, c))
                    effort[r - 1][c] = nxt_e
            if c > 0:
                nxt_e = max(e, abs(heights[r][c - 1] - heights[r][c]))
                if nxt_e < effort[r][c - 1]:
                    heapq.heappush(q, (nxt_e, r, c - 1))
                    effort[r][c - 1] = nxt_e
        return effort[row - 1][col - 1]
