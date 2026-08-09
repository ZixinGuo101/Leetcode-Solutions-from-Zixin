class Solution:
    def __init__(self):
        self.trie = {}
        self.ans = []
    
    def build_trie(self, words: List[str]):
        for word in words:
            p = self.trie
            for char in word:
                p[char] = p.setdefault(char, {})
                p = p[char]
            p[''] = True
        return
    
    def find(self, d: dict, path: List[str]):
        if '' not in d:
            return
        
        self.compare_path(path)
        for key in sorted(d):
            path.append(key)
            if key != '':
                self.find(d[key], path)
            path.pop()

    
    def compare_path(self, path: List[str]):
        if len(path) > len(self.ans):
            self.ans = path[:]
            return

    def longestWord(self, words: List[str]) -> str:
        self.build_trie(words)
        for key in sorted(self.trie):
            path = [key]
            self.find(self.trie[key], path)
        return ''.join(self.ans)

