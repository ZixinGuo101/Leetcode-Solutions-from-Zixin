class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def searchLeft(nums, target):
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) / 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] >= target:
                    r = mid - 1
            
            if l >= len(nums):
                return -1
            if nums[l] != target:
                return -1
            
            return l
        
        def searchRight(nums, target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) / 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] <= target:
                    l = mid + 1
            
            if r < 0:
                return -1
            if nums[r] != target:
                return -1
            
            return r
        
        return [searchLeft(nums, target), searchRight(nums, target)]

        