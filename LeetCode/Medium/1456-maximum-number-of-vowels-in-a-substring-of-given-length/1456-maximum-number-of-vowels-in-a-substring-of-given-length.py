class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = vowel = 0
        for i, c in enumerate(s):
            if c in "aeiou":
                vowel += 1
            
            left = i - k + 1
            if left < 0:
                continue
            
            res = max(res, vowel)
            
            if s[left] in "aeiou":
                vowel -= 1
        return res
        