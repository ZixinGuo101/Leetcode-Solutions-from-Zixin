class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        counts = [0] * (n+1)
        counts[0] = 1
        counts[1] = 1
        for nodes in range(2, n+1):
            pos = nodes // 2
            for root in range(1, pos+1):
                counts[nodes] += counts[root-1] * counts[nodes-root]
            counts[nodes] *= 2
            if nodes % 2 == 1:
                counts[nodes] += counts[pos] ** 2
        return counts[n]