class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        parts = input.split('\n')
        ans = 0
        stack = [-1]
        for part in parts:
            level = part.rfind('\t') + 1
            while level + 1 < len(stack):
                stack.pop()
            stack.append(len(part) - level + stack[-1] + 1)
            if '.' in part:
                ans = stack[-1] if stack[-1] > ans else ans
        
        return ans
            