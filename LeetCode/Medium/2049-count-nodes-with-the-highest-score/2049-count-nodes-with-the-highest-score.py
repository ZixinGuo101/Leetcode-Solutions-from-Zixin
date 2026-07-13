class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        self.res = 0
        self.max_score = 0
        graph = [[] for _ in range(n)]
        for c in range(1, n):
            graph[parents[c]].append(c)

        def count(node):
            score = 1
            total = 0
            for child in graph[node]:
                cn = count(child)
                score *= cn
                total += cn
            if total + 1 < n:
                score *= n - total - 1
            if score > self.max_score:
                self.max_score = score
                self.res = 1
            elif score == self.max_score:
                self.res += 1
            return total + 1
        
        count(0)
        return self.res
