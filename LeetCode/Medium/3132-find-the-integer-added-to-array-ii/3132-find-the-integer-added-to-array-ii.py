class Solution(object):
    def minimumAddedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        nums1.sort()
        nums2.sort()
        m = len(nums1)
        n = len(nums2)
        ans = float('inf')

        for i in range(2, 0, -1):
            d = nums2[0] - nums1[i]
            j = 1
            for num1 in nums1[i+1:]:
                # print(num1)
                if num1 + d == nums2[j]:
                    j += 1
                    print(j)
                    if j == n:
                        return d
        
        return nums2[0] - nums1[0]