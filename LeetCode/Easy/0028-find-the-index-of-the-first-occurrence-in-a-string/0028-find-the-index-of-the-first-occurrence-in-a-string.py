class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)

        if m < n:
            return -1
        
        d = set([needle])
        for l in range(m-n+1):
            sub = haystack[l:l+n]
            if sub in d:
                return l
        
        return -1
        