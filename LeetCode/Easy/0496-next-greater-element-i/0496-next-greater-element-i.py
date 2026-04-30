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

        for i in range(m-1, -1, -1):
            while st and nums2[i] > st[-1]:
                st.pop()
            if st and nums2[i] in d:
                idx = d[nums2[i]]
                res[idx] = st[-1]
            st.append(nums2[i])
        
        return res
