class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = n.bit_length()
        return (1 << l) - 1