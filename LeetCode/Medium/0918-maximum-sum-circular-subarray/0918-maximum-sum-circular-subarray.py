class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minq = deque()
        res = float('-inf')
        n = len(nums)
        pre_sum = [0] * (2*n+1)
        start = 0
        for end in range(1, 2*n+1):
            pre_sum[end] = pre_sum[end-1] + nums[(end-1) % n]
            if minq and end - minq[0] > n:
                minq.popleft()
            if minq:
                res = max(res, pre_sum[end] - pre_sum[minq[0]])
            while minq and pre_sum[minq[-1]] >= pre_sum[end]:
                minq.pop()
            minq.append(end)
        return res
