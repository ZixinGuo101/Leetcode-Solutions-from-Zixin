class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n & k != k:
            return -1
        s = n ^ k
        res = 0
        while s:
            s = s & (s - 1)
            res += 1
        return res