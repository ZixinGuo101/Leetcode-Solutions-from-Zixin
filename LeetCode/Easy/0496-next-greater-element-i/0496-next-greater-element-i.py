class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        m = self.monoStack(nums2)
        # print(m)
        for num in nums1:
            res.append(m[num])
        return res

    
    def monoStack(self, nums):
        n = len(nums)
        res = dict()
        stack = []

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                prev = stack.pop()
                res[nums[prev]] = nums[i]
            stack.append(i)
        while stack:
            cur = stack.pop()
            res[nums[cur]] = -1
        return res