class Solution:
    def longestWord(self, words: List[str]) -> str:
        s = set(words)
        s.add("")
        ans = ""
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and ans > word:
                if all(word[0:i] in s for i in range(1, len(word))):
                    ans = word
        return ans