class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        n = len(s)
        m = len(spaces)
        ans = []
        i = 0
        for j in range(n):
            if i < m and spaces[i] == j:
                ans.append(' ')
                i += 1
            ans.append(s[j])
        
        return ''.join(ans)