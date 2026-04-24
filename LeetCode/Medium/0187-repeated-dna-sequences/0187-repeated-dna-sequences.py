class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = set()
        d = set()
        n = len(s)

        for r in range(9, n):
            sub = s[r-9:r+1]
            if sub in d:
                ans.add(sub)
            else:
                d.add(sub)
        
        return list(ans)