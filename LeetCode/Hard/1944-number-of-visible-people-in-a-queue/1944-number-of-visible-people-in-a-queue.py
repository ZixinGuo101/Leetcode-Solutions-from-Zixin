class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0] * n
        stk = [n-1]
        for i in range(n-2, -1, -1):
            while stk and heights[i] > heights[stk[-1]]:
                stk.pop()
                ans[i] += 1
            if stk:
                ans[i] += 1
            stk.append(i)
        return ans