class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [False] * n
        def can_find(node):
            if arr[node] == 0:
                return True
            if visited[node]:
                return False
            visited[node] = True
            l = node - arr[node]
            if l >= 0 and not visited[l] and can_find(l):
                return True
            r = node + arr[node]
            if r < n and not visited[r] and can_find(r):
                return True
            return False
        return can_find(start)