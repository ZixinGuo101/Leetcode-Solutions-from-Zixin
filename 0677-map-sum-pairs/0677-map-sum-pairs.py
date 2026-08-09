class MapSum:

    def __init__(self):
        self.trie = {}
        self.trie[''] = 0
        self.pair = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.pair:
            val, self.pair[key] = val - self.pair[key], val
        else:
            self.pair[key] = val
        p = self.trie
        for char in key:
            if char not in p:
                p[char] = {}
            p = p[char]
            p[''] = p.get('', 0) + val

    def sum(self, prefix: str) -> int:
        p = self.trie
        total = 0
        for char in prefix:
            if char in p:
                p = p[char]
            else:
                return 0
        return p['']
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)