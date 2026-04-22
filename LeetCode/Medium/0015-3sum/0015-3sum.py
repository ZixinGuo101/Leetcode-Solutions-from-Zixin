class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = list()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            print(num)
            cnt = -num
            l = i+1
            r = n-1

            while l < r:
                sn = nums[l] + nums[r]
                ln, rn = nums[l], nums[r]
                if  sn < cnt:
                    l += 1   
                elif sn > cnt:
                    r -= 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                while l < r and nums[l] == ln:
                    l += 1
                while l < r and nums[r] == rn:
                    r -= 1
                
        
        return ans
        