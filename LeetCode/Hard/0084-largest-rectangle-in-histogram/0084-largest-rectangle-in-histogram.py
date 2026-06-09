class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        PrevLess = [-1] * n
        pstk = []
        NextLess = [n] * n
        nstk = []
        for i in range(n):
            while pstk and heights[pstk[-1]] >= heights[i]:
                pstk.pop()
            if pstk:
                PrevLess[i] = pstk[-1]
            pstk.append(i)
            while nstk and heights[nstk[-1]] >= heights[n-1-i]:
                nstk.pop()
            if nstk:
                NextLess[n-1-i] = nstk[-1]
            nstk.append(n-1-i)
        print(PrevLess)
        print(NextLess)
        res = 0
        for i in range(n):
            temp = heights[i] * (NextLess[i] - PrevLess[i] - 1)
            res = max(res, temp)
        
        return res