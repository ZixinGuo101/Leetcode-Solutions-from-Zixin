class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        m = self.monoStack(nums2)
        for num in nums1:
            res.append(m[num])
        return res

    
    def monoStack(self, nums):
        n = len(nums)
        res = dict()
        stack = []

        for i in range(n-1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            res[nums[i]] = -1 if not stack else stack[-1]
            stack.append(nums[i])
        
        return res