class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l = n
        r = -1
        lstk = []
        rstk = []
        for i in range(n):
            while lstk and nums[lstk[-1]] > nums[i]:
                l = min(l, lstk.pop())
                # print("l = ", l)
            lstk.append(i)
            while rstk and nums[rstk[-1]] < nums[n-1-i]:
                r = max(r, rstk.pop())
                # print("r = ", r)
            rstk.append(n-1-i)
        if l == n and r == -1:
            return 0
        return r - l + 1

