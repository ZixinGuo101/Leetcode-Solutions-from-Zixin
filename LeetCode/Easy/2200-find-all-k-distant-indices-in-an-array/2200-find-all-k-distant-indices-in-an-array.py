class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        l = 0
        r = -1001
        ans = []

        while i < n:
            if nums[i] != key:
                i += 1
                continue
            
            if (i - k) > r:
                if (i - k) > 0:
                    l = i - k
                else:
                    l = 0
            else:
                l = r + 1
            
            if (i + k) < n:
                r = i + k
            else:
                r = n - 1
            # print(l, r)
            ans += [x for x in range(l, r+1)]
            i += 1
            if r == n - 1:
                break
        
        return ans
            
        