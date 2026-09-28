class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        l1, l2 = 0, 0
        prev1, prev2 = 0, 0
        output = 0
        for cur1, cur2 in zip(nums1, nums2):
            next1, next2 = 1, 1
            if cur1 >= prev1:
                next1 = l1 + 1
            if cur1 >= prev2 and next1 < l2+1:
                next1 = l2 + 1
            if cur2 >= prev1:
                next2 = l1 + 1
            if cur2 >= prev2 and next2 < l2+1:
                next2 = l2 + 1
            l1, l2 = next1, next2
            prev1, prev2 = cur1, cur2
            output = max(output, l1, l2)
        
        return output
