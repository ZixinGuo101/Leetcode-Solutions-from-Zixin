class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        k = 1
        n = len(nums)
        cnt = 1

        for f in range(1, n):
            if nums[f] == nums[s]:
                if cnt == 2:
                    continue
                else:
                    cnt += 1
                    s += 1
                    nums[s] = nums[f]
                    k += 1
            else:
                cnt = 1
                s += 1
                nums[s] = nums[f]
                k += 1
        
        return k