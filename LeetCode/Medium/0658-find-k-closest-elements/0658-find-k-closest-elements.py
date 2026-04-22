class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        idx = n
        for i, num in enumerate(arr):
            if num >= x:
                idx = i
                break
        if idx == n:
            l = n-2
            r = n-1
        else:
            l = idx-1
            r = idx
        # print(l,r)
        cnt = 0
        while l >= 0 and r < n and cnt < k:
            ld = abs(x - arr[l])
            rd = abs(arr[r] - x)
            if ld <= rd:
                l -= 1
            else:
                r += 1
            cnt += 1
            # print(l,r,cnt)
        
        if l < 0:
            return arr[0:k]
        if r >= n:
            return arr[n-k:]
        
        return arr[l+1:r]
