class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0

        for c in s:
            if c == '(':
                left += 1
            else:
                if left == 0:
                    right += 1
                else:
                    left -= 1
        
        return left + right