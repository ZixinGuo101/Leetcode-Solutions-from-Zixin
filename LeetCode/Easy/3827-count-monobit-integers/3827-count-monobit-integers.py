class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        n += 1
        while n:
            n = n >> 1
            res += 1
        return res