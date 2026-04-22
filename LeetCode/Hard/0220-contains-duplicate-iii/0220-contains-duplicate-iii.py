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
            k = num // ds
            if k in d:
                return True
            if k-1 in d and abs(num - d[k-1]) <= valueDiff:
                return True
            if k+1 in d and abs(d[k+1] - num) <= valueDiff:
                return True

            d[k] = num
            if right - indexDiff >= 0:
                del d[nums[right - indexDiff] // ds]

        return False
        