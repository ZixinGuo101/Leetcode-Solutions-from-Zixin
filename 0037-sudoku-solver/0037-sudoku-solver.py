class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(m)]
        boxes = [set() for _ in range(m)]
        self.found = False

        def getBoxIndex(r, c):
            return (r // 3) * 3 + c // 3

        def isValid(r, c, ch):
            if ch in rows[r] or ch in cols[c] or ch in boxes[getBoxIndex(r, c)]:
                return False
            return True
        
        def backtrack(idx):
            if self.found:
                return
            r = idx // m
            c = idx % m
            if idx == m * n:
                self.found = True
                return
            if board[r][c] != ".":
                backtrack(idx + 1)
                return
            for ch in '123456789':
                if not isValid(r, c, ch):
                    continue
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[getBoxIndex(r, c)].add(ch)
                backtrack(idx + 1)
                if self.found:
                    return
                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[getBoxIndex(r, c)].remove(ch)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[getBoxIndex(i, j)].add(board[i][j])
        backtrack(0)
        return