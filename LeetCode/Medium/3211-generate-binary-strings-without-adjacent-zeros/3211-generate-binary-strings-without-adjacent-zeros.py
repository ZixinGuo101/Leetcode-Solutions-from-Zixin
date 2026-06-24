class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.res = []
        self.path = 0
        self.l = n
        self.build(n)
        return self.res

    def build(self, n):
        if n == 1:
            if self.path & 1 or n == self.l:
                self.path <<= 1
                self.res.append(format(self.path, 'b').zfill(self.l))
                self.path >>= 1
            self.path = (self.path << 1) | 1
            self.res.append(format(self.path, 'b').zfill(self.l))
            self.path >>= 1
            return
        
        if self.path & 1 or n == self.l:
            self.path <<= 1
            self.build(n-1)
            self.path >>= 1
        self.path = (self.path << 1) | 1
        self.build(n-1)
        self.path >>= 1
        return
