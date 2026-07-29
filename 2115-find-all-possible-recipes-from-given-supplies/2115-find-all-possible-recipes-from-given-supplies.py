class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = {}
        for r, ing in zip(recipes, ingredients):
            for s in ing:
                graph[s].append(r)
            in_degree[r] = len(ing)
        q = deque(supplies)
        res = []
        while q:
            cur = q.popleft()
            for node in graph[cur]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    q.append(node)
                    res.append(node)
        return res