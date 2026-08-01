class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        combination = []
        self.total = 0
        n = len(candidates)
        def backtrack(start):
            if self.total == target:
                res.append(combination.copy())
                return
            if self.total > target:
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                combination.append(candidates[i])
                self.total += candidates[i]
                backtrack(i + 1)
                self.total -= candidates[i]
                combination.pop()
        backtrack(0)
        return res