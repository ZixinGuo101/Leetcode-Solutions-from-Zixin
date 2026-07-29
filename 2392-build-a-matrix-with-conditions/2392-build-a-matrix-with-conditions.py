class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def order(Condition: List[List[int]]) -> List[int]:
            pos = [-1] * k
            graph = [[] for _ in range(k)]
            indeg = [0] * k
            count = 0
            for x, y in Condition:
                graph[x-1].append(y-1)
                indeg[y-1] += 1
            q = deque(i for i, d in enumerate(indeg) if d == 0)
            while q:
                cur = q.popleft()
                pos[cur] = count
                count += 1
                for nxt in graph[cur]:
                    indeg[nxt] -= 1
                    if indeg[nxt] == 0:
                        q.append(nxt)
            return pos if count == k else []
        
        row_list = order(rowConditions)
        col_list = order(colConditions)
        # print(row_list)
        # print(col_list)
        if len(row_list) == 0 or len(col_list) == 0:
            return []
        res = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):

            res[row_list[i]][col_list[i]] = i + 1
        return res

        


