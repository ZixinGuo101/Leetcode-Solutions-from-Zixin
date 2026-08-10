class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g =[[] for _ in range(n)]
        for x, y in dislikes:
            g[x-1].append(y-1)
            g[y-1].append(x-1)
        color = [0] * n
        def can_color(x, c):
            color[x] = c
            for y in g[x]:
                if color[y] == c or color[y] == 0 and not can_color(y, 3-c):
                    return False
            return True
        
        for i, c in enumerate(color):
            if c == 0 and not can_color(i, 1):
                return False
        return True