class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def EatingHours(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours
        
        # piles.sort()
        l = 1
        r = max(piles)

        while l <= r:
            mid = l + ( r - l) // 2
            t = EatingHours(mid)
            # print(mid, t)
            if t > h:
                l = mid + 1
            elif t < h:
                r = mid - 1
            elif t == h:
                r = mid - 1
        
        return l

        