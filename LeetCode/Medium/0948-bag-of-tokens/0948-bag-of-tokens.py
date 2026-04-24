class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        '''
        if len(tokens) == 0 or tokens[0] > power:
            return 0
        
        if len(tokens) == 1:
            return 1
        '''
        
        l = 0
        r = len(tokens) - 1

        ans = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                ans += 1
            elif r-1 > l and ans > 0:
                power += tokens[r]
                ans -= 1
                r -= 1
            else:
                return ans
        
        return ans
                