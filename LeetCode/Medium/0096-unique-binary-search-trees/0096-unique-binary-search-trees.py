class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        counts = [1] * (n+1)
        counts[2] = 2
        for idx in range(3, n+1):
            times = idx // 2
            idxSum = 0
            for i in range(times):
                idxSum += counts[i] * counts[idx-i-1]
            idxSum = idxSum * 2
            if idx % 2 == 1:
                idxSum += counts[times] ** 2
            counts[idx] = idxSum
        return counts[n]