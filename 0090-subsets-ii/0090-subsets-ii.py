class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        def backtrack(start):
            res.append(subset.copy())
            for i in range(start, n):
                if nums[i] == nums[i - 1] and i > start:
                    continue
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
        nums.sort()
        backtrack(0)
        return res