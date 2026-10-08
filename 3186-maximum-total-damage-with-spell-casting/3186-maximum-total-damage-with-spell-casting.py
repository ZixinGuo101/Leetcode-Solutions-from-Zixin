class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        a = sorted(cnt)

        @cache  # 缓存装饰器，避免重复计算 dfs（一行代码实现记忆化）
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            x = a[i]
            j = i
            while j and a[j - 1] >= x - 2:
                j -= 1
            return max(dfs(i - 1), dfs(j - 1) + x * cnt[x])

        return dfs(len(a) - 1)