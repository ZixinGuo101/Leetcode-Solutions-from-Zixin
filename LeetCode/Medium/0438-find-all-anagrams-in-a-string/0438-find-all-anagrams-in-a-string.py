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
        
        d = dict()
        for i in range(n):
            d[p[i]] = d.get(p[i], 0) - 1

        valid = len(d)
        cnt = 0
        for right, c in enumerate(s):
            if c in d:
                d[c] += 1
                if d[c] == 0:
                    cnt += 1
            
            left = right - n + 1
            if left < 0:
                continue

            if cnt == valid:
                ans.append(left)
            
            if s[left] in d:
                if d[s[left]] == 0:
                    cnt -= 1
                d[s[left]] -= 1
            left += 1

        return ans
        