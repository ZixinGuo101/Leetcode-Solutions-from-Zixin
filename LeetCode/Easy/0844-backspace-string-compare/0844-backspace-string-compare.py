class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        cntsb = 0
        cnttb = 0
        sr = len(s) - 1
        tr = len(t) - 1

        while sr >= 0 or tr >= 0:
            while sr >= 0:
                if s[sr] == '#':
                    cntsb += 1
                    sr -= 1
                elif cntsb > 0:
                    sr -= 1
                    cntsb -= 1
                else:
                    break
            
            while tr >= 0:
                if t[tr] == '#':
                    cnttb += 1
                    tr -= 1
                elif cnttb > 0:
                    tr -= 1
                    cnttb -= 1
                else:
                    break
            
            if sr >= 0 and tr >= 0:
                if s[sr] != t[tr]:
                    return False
            elif sr != tr:
                    return False
            
            sr -= 1
            tr -= 1
        
        return True