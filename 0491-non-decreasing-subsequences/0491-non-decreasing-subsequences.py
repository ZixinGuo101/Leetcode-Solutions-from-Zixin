class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        track = []

        def backtrack(start):
            if len(track) >= 2:
                ans.append(track[:])
            used = set()
            for i in range(start, len(nums)):
                if (track and track[-1] > nums[i]) or nums[i] in used:
                    continue
                used.add(nums[i])
                track.append(nums[i])
                backtrack(i + 1)
                track.pop()
        
        backtrack(0)
        return ans