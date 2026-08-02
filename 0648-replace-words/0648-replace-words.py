class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        self.tire = {}

        def build_tire(root: str):
            node = self.tire
            for char in root:
                node = node.setdefault(char, {})
            node[''] = True
        def find_root(word: str):
            res = 0
            node = self.tire
            for char in word:
                if char not in node:
                    return len(word)
                res += 1
                node = node[char]
                if '' in node:
                    return res
            return len(word)

        for root in dictionary:
            build_tire(root)
        for idx, word in enumerate(words):
            length = find_root(word)
            words[idx] = word[:length]
        return ' '.join(words)