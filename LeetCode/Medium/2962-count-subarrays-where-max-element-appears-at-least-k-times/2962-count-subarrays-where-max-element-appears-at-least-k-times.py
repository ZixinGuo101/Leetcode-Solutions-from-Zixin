class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_num = max(nums)
        max_num_t = 0
        left = 0
        ans = 0
        '''
        for i, num in enumerate(nums):
            max_num = num if num > max_num else max_num
        '''


        for right, num in enumerate(nums):
            if num == max_num:
                max_num_t += 1
            
            while max_num_t >= k:
                if nums[left] == max_num:
                    max_num_t -= 1
                left += 1
            
            ans += left
                    
        return ans

        