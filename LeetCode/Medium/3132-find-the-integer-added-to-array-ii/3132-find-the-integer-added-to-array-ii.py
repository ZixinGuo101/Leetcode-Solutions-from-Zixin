class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        def eq(i):
            d = nums2[0] - nums1[i]
            l1 = i + 1
            l2 = 1
            while l1 < m and l2 < n:
                while l1 < m and nums1[l1] + d != nums2[l2]:
                    l1 += 1
                if l1 >= m:
                    return False
                l1 += 1
                l2 += 1
            
            return l2 == n

        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        ans = float('inf')

        for i in range(3):
            if eq(i):
                d = nums2[0] - nums1[i]
                ans = d if d < ans else ans
        
        return ans