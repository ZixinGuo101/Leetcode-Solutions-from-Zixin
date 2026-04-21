class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt0 = 0
        cnt1 = 0
        left = 0
        ans  = 0

        for right, c in enumerate(s):
            if c == '0':
                cnt0 += 1
            else:
                cnt1 += 1

            while cnt0 > k and cnt1 > k:
                if s[left] == '0':
                    cnt0 -= 1
                else:
                    cnt1 -= 1
                left += 1
            
            ans += right - left + 1
        
        return ans