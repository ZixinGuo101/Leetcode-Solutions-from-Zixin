class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        parenthesis = []
        
        def backtrack(left, right):
            if left == right and left == n:
                ans.append(''.join(parenthesis))
                return
            if left < n:
                parenthesis.append('(')
                backtrack(left + 1, right)
                parenthesis.pop()
            if left > right:
                parenthesis.append(')')
                backtrack(left, right + 1)
                parenthesis.pop()
        
        backtrack(0, 0)
        return ans

