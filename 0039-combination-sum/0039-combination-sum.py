class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []
        total = [0]
        n = len(candidates)
        def backtrack(start):
            if total[0] == target:
                res.append(combination[:])
            for i in range(start, n):
                if candidates[i] > target or total[0] + candidates[i] > target:
                    return
                total[0] += candidates[i]
                combination.append(candidates[i])
                backtrack(i)
                total[0] -= candidates[i]
                combination.pop()
        backtrack(0)
        return res
            
