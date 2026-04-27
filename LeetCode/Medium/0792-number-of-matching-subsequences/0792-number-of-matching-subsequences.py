class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def FindLeft(target, sList):
            l = 0
            r = len(sList) - 1
            while l <= r:
                mid = l + (r - l) / 2
                if sList[mid] == (target + 1):
                    r = mid - 1
                elif sList[mid] < (target + 1):
                    l = mid + 1
                elif sList[mid] > (target + 1):
                    r = mid - 1
            return l
        
        def Issub(d, word):
            if word[0] not in d:
                return False
            else:
                j = d[word[0]][0]
            i = 1
            n = len(word)
            while i < n:
                if word[i] not in d:
                    return False
                # print(j, d[word[i]])
                pos = FindLeft(j, d[word[i]])
                if pos == len(d[word[i]]):
                    return False
                j = d[word[i]][pos]
                i += 1
            
            return True


        d = dict()
        for i, c in enumerate(s):
            if c in d:
                d[c].append(i)
            else:
                d[c] = [i]
        
        ans = 0
        for word in words:
            if Issub(d, word):
                # print(word)
                ans += 1
        
        return ans