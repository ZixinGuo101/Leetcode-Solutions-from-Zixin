class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
                continue
            s2 = stack.pop()
            s1 = stack.pop()
            if token == '+':
                s = s1 + s2
            elif token == '-':
                s = s1 - s2
            elif token == '*':
                s = s1 * s2
            else:
                s = s1 // s2
                if s < 0 and s1 % s2 != 0:
                    s += 1
            stack.append(s)
            # print(s)
        
        return stack[0]