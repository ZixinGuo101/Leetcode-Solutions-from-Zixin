class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = 0
        n = k * threshold
        count = 0

        for right, num in enumerate(arr):
            count += num

            left = right - k + 1
            if left < 0:
                continue
            
            if count >= n:
                res += 1
            
            count -= arr[left]
            left += 1
        
        return res
        