class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        res = n + 1
        minq = deque([0])
        pre_sum = [0] * (n + 1)
        for i in range(1, n+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
            while minq and pre_sum[minq[-1]] >= pre_sum[i]:
                minq.pop()
            minq.append(i)

            while minq and pre_sum[i] - pre_sum[minq[0]] >= k:
                res = min(res, i - minq.popleft())
        
        return -1 if res == n+1 else res