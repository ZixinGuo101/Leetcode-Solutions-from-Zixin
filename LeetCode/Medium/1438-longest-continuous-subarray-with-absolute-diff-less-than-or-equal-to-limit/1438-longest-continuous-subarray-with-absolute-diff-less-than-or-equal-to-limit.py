class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        maxq = deque()
        minq = deque()
        n = len(nums)
        start = 0
        res = 0
        for end in range(n):
            while maxq and maxq[-1] < nums[end]:
                maxq.pop()
            maxq.append(nums[end])
            while minq and minq[-1] > nums[end]:
                minq.pop()
            minq.append(nums[end])
            while start < end and (maxq[0] - minq[0]) > limit:
                if nums[start] == maxq[0]:
                    maxq.popleft()
                if nums[start] == minq[0]:
                    minq.popleft()
                start += 1
            # print(start, end)
            res = max(res, end - start + 1)
        return res