class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def match(q):
            n = len(q)
            ql = 0
            pl = 0
            while pl < pn:
                while ql < n and q[ql] != pattern[pl] and q[ql].islower():
                    ql += 1
                
                if ql == n or q[ql] != pattern[pl]:
                    return False
                pl += 1
                ql += 1
            
            while ql < n and q[ql].islower():
                ql += 1
            
            return ql == n
        
        pn = len(pattern)
        ans = []

        return [match(qq) for qq in queries]