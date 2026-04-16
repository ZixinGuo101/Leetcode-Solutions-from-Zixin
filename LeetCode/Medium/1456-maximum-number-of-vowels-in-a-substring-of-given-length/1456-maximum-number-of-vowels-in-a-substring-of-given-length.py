class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        def isVowels(c):
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                return True
            else:
                return False
        
        count = 0
        for i in range(k):
            if isVowels(s[i]) is True:
                count += 1
        
        res = count
        # print(res)
        back = 0
        front = k-1
        while front < len(s)-1:

            if isVowels(s[back]) is True:
                count -= 1
            back += 1
            front += 1
            if isVowels(s[front]) is True:
                count += 1
             
            res = max(res, count)
        
        return res
        