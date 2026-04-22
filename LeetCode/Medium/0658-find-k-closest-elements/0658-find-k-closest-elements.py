class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = 0
        r = len(arr) - 1

        while l < r and (r - l + 1 > k):
            ld = abs(arr[l] - x)
            rd = abs(arr[r] - x)
            if ld <= rd:
                r -= 1
            else:
                l += 1
        
        return arr[l:l+k]
        