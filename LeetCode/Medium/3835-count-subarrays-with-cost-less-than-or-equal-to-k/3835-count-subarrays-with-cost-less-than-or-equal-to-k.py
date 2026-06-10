class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        maxq = deque()
        minq = deque()
        l = 0
        res = 0
        for r in range(n):
            while maxq and nums[maxq[-1]] < nums[r]:
                maxq.pop()
            maxq.append(r)
            while minq and nums[minq[-1]] > nums[r]:
                minq.pop()
            minq.append(r)
            while l <= r and (nums[maxq[0]] - nums[minq[0]]) * (r - l + 1) > k:
                if l == maxq[0]:
                    maxq.popleft()
                if l == minq[0]:
                    minq.popleft()
                l += 1
            res += r - l + 1
        return res