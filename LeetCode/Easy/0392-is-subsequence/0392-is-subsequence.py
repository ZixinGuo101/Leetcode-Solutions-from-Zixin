class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sn = len(s)
        tn = len(t)
        sl = 0
        tl = 0
        while sl < sn:
            while tl < tn and t[tl] != s[sl]:
                tl += 1
            if tl >= tn:
                return False
            tl += 1
            sl += 1
        
        return True