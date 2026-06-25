class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cnt = {}
        cnt[0] = 1
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            if (pre - k) in cnt:
                res += cnt[pre - k]
            cnt[pre] = cnt.get(pre, 0) + 1
        return res