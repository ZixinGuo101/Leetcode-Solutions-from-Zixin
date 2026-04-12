class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        
        # 2 5 6 0 0 0, 1 2 3
        l1 = m - 1
        l2 = n - 1
        ln = m + n - 1

        while ln >= 0:
            if l2 < 0:
                return
            elif l1 < 0:
                nums1[ln] = nums2[l2]
                l2 -= 1
            elif nums1[l1] > nums2[l2]:
                nums1[ln] = nums1[l1]
                l1 -= 1
            else:
                nums1[ln] = nums2[l2]
                l2 -= 1
            ln -= 1


        