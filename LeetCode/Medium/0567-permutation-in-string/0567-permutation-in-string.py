class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        
        d = [0] * 26
        for i in range(m):
            d[ord(s1[i]) - ord('a')] += 1
        
        left = 0
        k = m
        for right, c in enumerate(s2):
            if d[ord(c) - ord('a')] > 0:
                k -= 1
            d[ord(c) - ord('a')] -= 1
            
            if right - m + 1 < 0:
                continue
            
            if k == 0:
                return True
            
            d[ord(s2[left]) - ord('a')] += 1
            if d[ord(s2[left]) - ord('a')] > 0:
                k += 1
            left += 1
        
        return False
        