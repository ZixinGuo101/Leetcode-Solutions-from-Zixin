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
            d[ord(s1[i]) - ord('a')] -= 1
        
        k = m
        for right, c in enumerate(s2):
            start = ord(c) - ord('a')
            if d[start] < 0:
                k -= 1
            d[ord(c) - ord('a')] += 1

            left = right - m + 1
            if left < 0:
                continue

            while k == 0:
                return True
            
            end = ord(s2[left]) - ord('a')
            d[end] -= 1
            if d[end] < 0:
                k += 1
            left += 1
        
        return False
        