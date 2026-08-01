class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        on_path = [False] * n
        path = [0] * n
        def backtrack(start):
            if start == n:
                res.append(path[:])
                return
            for i in range(n):
                if on_path[i] or i > 0 and nums[i] == nums[i - 1] and not on_path[i - 1]:
                    continue
                on_path[i] = True
                path[start] = nums[i]
                backtrack(start + 1)
                on_path[i] = False
        backtrack(0)
        return res
