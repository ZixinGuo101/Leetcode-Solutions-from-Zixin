class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def CalculateK(ms):
            ks = 1
            cnt = ms
            for num in nums:
                if cnt - num >= 0:
                    cnt -= num
                else:
                    ks += 1
                    cnt = ms - num
            return ks
        
        l = max(nums)
        r = sum(nums)

        while l <= r:
            mid = l + (r - l) // 2
            mk = CalculateK(mid)
            if mk < k:
                r = mid - 1
            elif mk > k:
                l = mid + 1
            else:
                r = mid - 1
        
        return l