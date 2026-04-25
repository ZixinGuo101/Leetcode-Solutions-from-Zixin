class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def Days(c):
            d = 1
            cnt = c
            for w in weights:
                if (cnt - w) >= 0:
                    cnt -= w
                else:
                    d += 1
                    cnt = c - w
            return d
        
        l = max(weights)
        r = sum(weights)
        # print(type(r), r)

        while l <= r:
            mid = l + (r - l) / 2
            md = Days(mid)
            # print(l, mid, r, md)
            if md > days:
                l = mid + 1
            elif md < days:
                r = mid - 1
            elif md == days:
                r = mid - 1
        
        return l
             
        