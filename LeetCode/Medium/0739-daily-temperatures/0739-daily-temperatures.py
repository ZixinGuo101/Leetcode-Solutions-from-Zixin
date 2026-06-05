class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [-1] * n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            res[i] = 0 if not stack else (stack[-1][1] - i)
            stack.append([temperatures[i], i])
        
        return res