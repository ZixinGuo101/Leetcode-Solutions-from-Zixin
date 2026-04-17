class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        count = 0
        indi = set()
        s = {}


        for right, num in enumerate(nums):
            if s.get(num, 0) != 0:
                indi.add(num)
                s[num] += 1
            else:
                s[num] = 1
            count += num

            left = right - k + 1
            if left < 0:
                continue
            
            if not indi:
                res = max(res, count)
            
            s[nums[left]] -= 1
            if s[nums[left]] == 1:
                indi.discard(nums[left])
            count -= nums[left]
        
        return res

        