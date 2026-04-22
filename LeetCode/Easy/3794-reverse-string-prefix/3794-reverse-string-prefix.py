class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left = 0
        right = k-1
        m = [''] * k
        while left <= right:
            m[left], m[right] = s[right], s[left]
            left += 1 
            right -= 1
        s1 = ''.join(m)
        return s1+s[k:]
        