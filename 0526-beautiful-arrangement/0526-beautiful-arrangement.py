class Solution:
    def countArrangement(self, n: int) -> int:
        self.visited = 1
        target = (1 << (n + 1)) - 1
        self.ans = 0

        def backtrack(pos):
            if self.visited == target:
                self.ans += 1
                return
            for i in range(1, n+1):
                if self.visited & (1 << i):
                    continue
                if i % pos == 0 or pos % i == 0:
                    self.visited += 1 << i
                    backtrack(pos + 1)
                    self.visited -= 1 << i

        for i in range(1, n+1):
            self.visited += 1 << i
            backtrack(2)
            self.visited -= 1 << i
        return self.ans