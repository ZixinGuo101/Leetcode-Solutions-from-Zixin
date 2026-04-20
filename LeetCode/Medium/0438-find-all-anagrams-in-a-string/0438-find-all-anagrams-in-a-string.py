class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m = len(s)
        n = len(p)
        ans = []
        if m < n:
            return ans
        
        d = [0] * 26
        for i in range(n):
            d[ord(p[i]) - ord('a')] += 1
        
        left = 0
        k = n
        for right, c in enumerate(s):
            if d[ord(c) - ord('a')] > 0:
                k -= 1
            d[ord(c) - ord('a')] -= 1
            
            if right - n + 1 < 0:
                continue
            
            if k == 0:
                ans.append(left)
            
            d[ord(s[left]) - ord('a')] += 1
            if d[ord(s[left]) - ord('a')] > 0:
                k += 1
            left += 1
        
        return ans


        