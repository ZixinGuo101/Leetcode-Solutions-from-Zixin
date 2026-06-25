class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        cnt = {}
        cnt[0] = 1
        res = 0
        pre = 0
        for i in range(len(nums)):
            pre ^= nums[i]
            if pre in cnt:
                res += cnt[pre]
            cnt[pre] = cnt.get(pre, 0) + 1
        return res