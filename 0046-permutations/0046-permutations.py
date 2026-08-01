class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        on_path = [False] * n
        path = []
        def traverse(i, t):
            if on_path[i]:
                return
            if t == n:
                path.append(nums[i])
                res.append(path.copy())
                path.pop()
                return
            on_path[i] = True
            path.append(nums[i])
            for j in range(n):
                traverse(j, t+1)
            on_path[i] = False
            path.pop()
        for i in range(n):
            traverse(i, 1)
        return res