class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {x : i for i, x in enumerate(nums1)}
        n = len(nums1)
        m = len(nums2)
        st = []
        res = [-1] * n

        for i in range(m):
            while st and nums2[i] > st[-1]:
                prev = st.pop()
                if prev in d:
                    idx = d[prev]
                    res[idx] = nums2[i]
            st.append(nums2[i])
        
        return res