class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        d_re = dict()
        d_su = dict()
        q = deque()
        num = 0
        for recipe in recipes:
            d_re[recipe] = num
            num += 1
        for supply in supplies:
            d_su[supply] = num
            q.append(num)
            num += 1
        graph = [[] for _ in range(len(recipes)+len(supplies))]
        in_degree = [0] * len(recipes)
        for i, ig in enumerate(ingredients):
            for food in ig:
                if food in d_re:
                    graph[d_re[food]].append(i)
                elif food in d_su:
                    graph[d_su[food]].append(i)
                in_degree[i] += 1
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    q.append(nxt)
                    res.append(recipes[nxt])
        return res