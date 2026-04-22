from sortedcontainers import SortedList
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        st = SortedList()

        for right, num in enumerate(nums):
            
            idx = st.bisect_left(num)
            if idx > 0 and abs(num - st[idx-1]) <= valueDiff:
                return True
            if idx < len(st) and abs(st[idx] - num) <= valueDiff:
                return True
            st.add(num)

            if (right - indexDiff) >= 0:
                st.remove(nums[right-indexDiff])
        
        return False