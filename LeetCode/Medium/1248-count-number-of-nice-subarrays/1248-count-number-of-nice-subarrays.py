class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        pre_cnt = 0
        d = {0:1}

        for i in range(len(nums)):
            if nums[i] & 1 == 1:
                pre_cnt += 1
            
            if pre_cnt - k in d:
                ans += d[pre_cnt-k]
            d[pre_cnt] = d.get(pre_cnt, 0) + 1
        
        return ans

        