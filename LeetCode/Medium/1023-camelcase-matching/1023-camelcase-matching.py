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
            while ql < n and pl < pn:
                # print(q[ql], q[ql] > 'Z')
                while ql < n and q[ql] != pattern[pl] and q[ql] > 'Z':
                    ql += 1
                # print(ql,pl)
                if ql < n and q[ql] != pattern[pl]:
                    return False
                elif ql >= n:
                    break
                else:
                    ql += 1
                    pl += 1
            
            if pl < pn:
                return False
            while ql < n:
                if q[ql] <= 'Z':
                    return False
                ql += 1
            
            return True

        ans = []
        pn = len(pattern)
        for qq in queries:
            ans.append(match(qq))
        
        return ans