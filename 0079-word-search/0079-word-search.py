class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        neigh = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        self.path = set()
        init = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    init.append((i, j))

        def findNeighbors(i, j):
            ans = []
            for nxt in neigh:
                n_i = i + nxt[0]
                n_j = j + nxt[1]
                if n_i >= 0 and n_i < m and n_j >= 0 and n_j < n:
                    ans.append((n_i, n_j))
            return ans

        def backtrack(i, j, idx):
            if idx == l:
                return True
            neighbors = findNeighbors(i, j)
            for nei in neighbors:
                if board[nei[0]][nei[1]] == word[idx] and nei not in self.path:
                    self.path.add(nei)
                    if backtrack(nei[0], nei[1], idx + 1):
                        return True
                    self.path.remove(nei)
            return False

        for i, j in init:
            self.path.add((i, j))
            if backtrack(i, j, 1):
                return True
            self.path.remove((i, j))
        return False

                