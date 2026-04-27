class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        n = len(nums1)
        ans = [0] * n
        idx = sorted(range(n), key = lambda i : nums2[i])
        # print(idx)

        l = 0
        r = n - 1

        for x in nums1:
            if x > nums2[idx[l]]:
                ans[idx[l]] = x
                l += 1
            else:
                ans[idx[r]] = x
                r -= 1
        
        return ans
