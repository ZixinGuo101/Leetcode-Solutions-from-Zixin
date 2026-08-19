class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        self.num = 0
        self.length = 1
        def backtrack(last_num):
            if self.length == n:
                ans.append(self.num)
                return
            self.num *= 10
            if last_num - k >= 0:
                last_num -= k
                self.num += last_num
                self.length += 1
                backtrack(last_num)
                self.num -= last_num
                last_num += k
                self.length -= 1
            if last_num + k <= 9 and k != 0:
                last_num += k
                self.num += last_num
                self.length += 1
                backtrack(last_num)
                self.num -= last_num
                last_num -= k
                self.length -= 1
            self.num = self.num // 10
            return
        
        for i in range(1, 10):
            self.num = i
            backtrack(i)
        return ans
