class State:
    def __init__(self):
        self.children = {}
        self.end = False
        self.n = 0

class Solution:
    def __init__(self):
        self.trie = State()

    def build_trie(self, words):
        for word in words:
            p = self.trie
            for char in word:
                if char not in p.children:
                    p.children[char] = State()
                p = p.children[char]
                p.n += 1
            p.end = True
    
    def count(self, word):
        p = self.trie
        total = 0
        for char in word:
            p = p.children[char]
            total += p.n
        return total

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.build_trie(words)
        ans = []
        for word in words:
            ans.append(self.count(word))
        return ans