class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        sa = sorted(arr)
        n = len(sa)
        if n == 1:
            return arr
        m = sa[(n-1)/2]
        l = 0
        r = n-1

        while l <= r and r - l + 1 > n - k:
            ld = abs(sa[l] - m)
            rd = abs(sa[r] - m)
            if rd >= ld:
                r -= 1
            else:
                l += 1
        
        return sa[:l] + sa[r+1:]
        