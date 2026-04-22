class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        d = dict()
        ds = valueDiff + 1

        for right, num in enumerate(nums):
            k = num // ds if num >= 0 else (num+1) // ds - 1

            if k in d:
                return True
            if k-1 in d and abs(num - d[k-1]) <= valueDiff:
                return True
            if k+1 in d and abs(d[k+1] - num) <= valueDiff:
                return True

            d[k] = num
            if right - indexDiff >= 0:
                left_num = nums[right - indexDiff]
                end = left_num // ds if left_num >= 0 else (left_num+1) // ds - 1
                del d[end]

        return False
        