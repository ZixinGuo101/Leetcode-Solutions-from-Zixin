class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        l = preorder.split(',')
        self.idx = -1
        def build():
            self.idx += 1
            if self.idx > len(l) - 1:
                return False
            if l[self.idx] == '#':
                return True
            return build() and build()
        return build() and self.idx == len(l) - 1