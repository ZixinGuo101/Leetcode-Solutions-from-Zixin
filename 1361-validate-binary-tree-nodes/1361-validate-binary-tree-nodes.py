class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = set(leftChild + rightChild)
        if len(children) != n:
            return False
        root = -1
        for i in range(n):
            if i not in children:
                root = i
                break
        visited = set()
        count = 0
        q = deque([root])
        while q:
            cur = q.popleft()
            if leftChild[cur] != -1:
                if leftChild[cur] in visited:
                    return False
                visited.add(leftChild[cur])
                q.append(leftChild[cur])
            if rightChild[cur] != -1:
                if rightChild[cur] in visited:
                    return False
                visited.add(rightChild[cur])
                q.append(rightChild[cur])
        return len(visited) == n-1