class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        def backtrack(i):
            res.append(subset.copy())
            for c in range(i+1, n):
                subset.append(nums[c])
                backtrack(c)
                subset.pop()
        backtrack(-1)
        return res    
        