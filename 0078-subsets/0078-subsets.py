class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n = len(nums)
        def backtrack(i):
            res.append(subset.copy())
            for c in range(i, n):
                subset.append(nums[c])
                backtrack(c + 1)
                subset.pop()
        backtrack(0)
        return res    
        