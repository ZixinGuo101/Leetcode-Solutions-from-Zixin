class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = dict()
        ans = []
        n = len(s)

        for right in range(9, n):
            left = right - 10 + 1
            sub = s[left:right+1]
            if sub in d and d[sub] == 1:
                d[sub] += 1
                ans.append(sub)
            else:
                d[sub] = d.get(sub, 0) + 1
        
        return ans

        