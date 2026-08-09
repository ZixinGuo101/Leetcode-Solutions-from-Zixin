class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        s = set()
        s.add("")
        ans = ""

        for word in words:
            if word[:-1] in s:
                s.add(word)
                if len(word) > len(ans):
                    ans = word
        
        return ans