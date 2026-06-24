class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.res = []
        self.path = 0
    
        def build(i: int) -> None:
            if i == n:
                self.res.append(f"{self.path:0{n}b}")
                return
            if i == 0 or self.path & 1:
                self.path <<= 1
                build(i+1)
                self.path >>= 1
            self.path = (self.path << 1) | 1
            build(i+1)
            self.path >>= 1
            return
        
        build(0)
        return self.res