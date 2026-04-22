class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s1 = s[k-1::-1]
        s2 = s[k:]
        return s1+s2