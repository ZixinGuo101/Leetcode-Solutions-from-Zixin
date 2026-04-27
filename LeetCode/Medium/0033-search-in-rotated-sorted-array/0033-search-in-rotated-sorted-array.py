class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        k = 0
        l = 1
        r = len(nums) - 1
        if nums[0] > nums[len(nums) - 1]:
            while l <= r:
                mid = l +(r - l) / 2
                if nums[mid] > nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            k = r+1
        print(k)
        if target == nums[len(nums) - 1]:
            return len(nums) - 1
        elif target < nums[len(nums) - 1]:
            l = k
            r = len(nums) - 1
        else:
            l = 0
            r = k
        
        while l <= r:
            print(l, r)
            mid = l + (r - l) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1

