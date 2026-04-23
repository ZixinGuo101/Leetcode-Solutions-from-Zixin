class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # -2 -1 0 0 0 0 0 0 1 2
        ans = list()
        nums.sort()
        n = len(nums)
        i = 0
        # print(nums)
        while i < n-3:
            j = i+1
            while j < n-2:
                cnt = target - nums[i] - nums[j]
                l = j+1
                r = n-1
                while l < r:
                    # print(l, r)
                    if (nums[l] + nums[r]) > cnt:
                        r -= 1
                    elif (nums[l] + nums[r]) < cnt:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        r -= 1
                        l += 1
                    
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                
                j += 1
                while j < n and nums[j] == nums[j-1]:
                    j += 1
            
            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
        
        return ans
        