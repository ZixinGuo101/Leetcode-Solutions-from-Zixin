class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False] * n
        path = []
        def backtrack():
            if len(path) == n:
                res.append(path.copy())
            for i in range(n):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtrack()
                visited[i] = False
                path.pop()
        backtrack()
        return res
